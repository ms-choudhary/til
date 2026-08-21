# Booting Linux on x86_64

When you power on a PC, a intricate handshake happens between several programs and literal CPU before you see the familiar screen. 

When power stabilises, CPU does a reset into a 16 bit real mode. Real mode is for backward compatibility to mimic older 8086 chip. All x86 processors (intel, amd etc) do this. 

CPU then jumps to reset vector at location: 0xFFFFFFF0 (special hardcode address). This is hardwired so every time a CPU resets, it always start here, like a permanent bookmark. This contains far jump to firmware on motherboard. 

### BIOS/UEFI

Firmware is software baked into the board. Stored on read only chip on motherboard. 

BIOS (Basic Input Output System) is the firmware, manufacture developed primitive software, which does:
- health check via POST (Power On Self Test), makes sure all critical hardware is working before booting into OS
- If there are any problems at this stage, machine beeps
- Looks at the boot order, and tries to load 1st stage boot. 
	- Any disk whose first sector (512 bytes), ends with 0x55 0xAA (magic bytes) is considered bootable (MBR). 
	- GUID Partition table (GPT for UEFI)
	- Net booting (for PXE)
- Copies that sector to memory at 0x7C00 address and jumps there. 

1 sector (512 bytes) boot loader is tiny, and it only knows how to load 2nd stage boot loader.

### UEFI

[[inbox/uefi]] is a modern firmware, overcomes the limitation of multi stage boot loading. It understand filesystems (FAT32) and can directly load bigger programs (can technically boot kernel without boot loader) without the limitation of 512 bytes. It can pass richer info to OS. 

UEFI also handles the steps of setup program below:
- Setup GDT, IDT, switch to protected mode
- Setup paging
- Switching to long mode

### SME

Some AMD CPUs has encrypt RAM feature called Secure Memory Encryption. 

### Segment & Offset

```
physical address = (segment << 4) + offset
```
### Grub

Grub boot loader understands filesystems, it loads the kernel into memory. Kernel file consists of:
- Small setup program, which runs in real mode (only in x86_64, non UEFI, for switching cpu from real -> protected -> long mode)
- Larger compressed kernel

Grub fills up setup headers like:
- Where kernel is placed
- Where command line lives
- Where is init rd etc

Finally it jumps to the setup program. 
### Interrupts

Interrupts can be hardware or software for handling real time events. On interrupt, CPU pauses the work and runs then handler in Interrupt Descriptor Table (IDT). Examples include, when key is pressed etc. It can be maskable, meaning temporary blocked to prevent firing during delicate moments. And Non Maskable (NMI) which always interrupt, it can indicate serious hardware issues. If you don't have handler entry in IDT, handler lookup fails, CPU gives up (triple fault) and resets silently. 

### CPU control registers

- CR0
	- Turns on the protected mode
- CR3
	- Holds the address of top of page table
- CR4
	- Enables extended features, for larger page table. 
- EFER
	- Switch to long mode
### Setup Program

Setup program, first creates a predictable workspace:
- Lines up segment registers, so memory copy behave the same way every time. It also sets "direction flag" CPU bit, so copy instructions auto moves the pointer forward through memory. 
- Creates stack, LIFO workbench, where functions store data temporarily. SS says which segment the stack uses and SP points to the top of the stack. 
- Clears BSS (where global variables reside), C code ensures that global variable will be initialised to zero. So it sets that area to 0. 
- Programs serial port to print early message, before graphics is setup
- Asks firmware for usable and reserved RAM ranges (there can be holes). On old BIOS this call is nick named e820. 
- Finally it calls the first c function literally called main. 

#### Protected mode

Modern linux runs in long mode: 64 bit in x86_64. But you can't go directly to that, you first transition from 32 bit real mode to 32 bit protected mode, finally to long mode. 

Protected mode consists of following ideas:
- Global Descriptor Table (GDT): list of segments with descriptions, for eg a segment starts here, covers this much and allowed to do these. 
- Interrupt Descriptor Table (IDT), aka phone numbers for emergency, when a interrupt arrives, CPU looks up entry in IDT for handler to call.  

Here's how setup program switches CPU into protected mode:
- Disables maskable interrupts, other than what's needed
- Loads the tiny GDT & IDT
- Sets single bit PE in control register, CR0. 
- Does a far jump. That jump reloads code segment from GDT, and locks it into protected mode. It reloads the data & stack segments. 
We're now in protected mode. 

### Paging

Finally we need to enable paging before we can switch to long mode. 

Programs use virtual address, while hardware reads and writes physical address. A page table translates virtual address into physical address, in fixed size chunks call pages. A typical page size is 4KB, earlier boot uses larger 2MB pages to layout low memory quickly. 

Initially, we build a small page table in 32 bit mode, called identity map, which means for this specific region, virtual address equals physical one. So we can flip on paging. 

Next it enables PAE bit in CR4 register so larger entries are used and builds a minimal table for lower memory. Writes the address of the top table in CR3. Paging is now ready. 

Finally we set LME bit in special register EFER, this switches the CPU in long mode.

### ELF
ELF short for Executable & Linkable Format, is both a file format and a map, which says what chunks are code, data etc and exactly where each chunk wants to live. 

### Decompressing kernel

We now have CPU running in 64 bit long mode with paging enabled, and compressed kernel in memory. 

Now, 64 bit small stub code takes over. First it figures out where it's running. Early code is linked as if it starts at address 0, it computes it real base at runtime. It relocates itself if it can overlap with uncompressed kernel (with KASLR). 

It loads a minimal IDT:
- Page fault handler: Page fault happens when CPU can't find the mapping for virtual address, in identity mapped world, handler adds the mapping on the fly. 
- NMI handler, so it doesn't crash the machine, while we're bringing things up. 

C func `extract_kernel` takes over and unpacks the kernel using algorithm it was built with (gzip, xz, zstd, lzo etc). 

Kernel itself like other binaries are packaged as ELF file. When bytes are out, decompressor reads the kernel's ELF headers. It copies the chunks to memory where it belongs. 

Next it jumps to real kernel `start_kernel`, and big initialisations begins. 

#### KASLR (Kernel Address Space Layout Randomisation)

If attacker don't know where the kernel actually lives in memory, a lot of attacks get harder. 

If KASLR is enabled, decompressor choses 2 bases at random:
- Physical base
- Virtual base

It first builds a do not touch list, which includes:
- decompressor itself 
- compressed kernel image
- initial ram disk
- boot params
- command line buffers
- also includes ranges reserved using `memmap=` option on command line

Scans memory map received earlier from the firmware and finds the ranges where everything can fit. It draws random number using the best early entropy source. On modern CPUs, it's `rand` instruction on hardware. [trusted-platform-module](/hardware/trusted-platform-module.md)

### Start Kernel

- `verify_cpu`, checks long mode support, verifies sse2, validates other cpu features. It fails here, to prevent running 64 bit kernel on 32 bit hardware. 
- [Microcode patching](/linux/booting-linux-on-x86-64.md#Microcode%20patching)
- resets the early identity mapped page tables
- clears bss, zeros out `.bss` section
- setups KASAN (Kernel Address Sanitizer)
- Copies bootloader data into kernel owned structs, to prevent overwriting. 
- `setup_arch()`
	- what can cpu do? Asks the chip directly using CPUID instructions. Dumps the data into boot_cpu_data struct for later lookups, for eg, do we've feature x? Helps in deciding if to use AVX512 memcpy instruction or fall back to slower one. 
- Cleans up the E820 memory map obtained from firmware. Feeds it into memblock, starts tracking free and reserved ranges, i.e., early memory allocator, before kmalloc or vmalloc. 
- If `earlyprintk=serial,ttyS0` command line flag passed, it sets up minimal serial driver. 
- Collects info about the machine
	- efi_init() hooks up UEFI runtime services
	- dmi_setup() firmware tables, describes motherboard, vendor, bios version etc
	- `init_hypervisor_platform()` - checks if we're on real hardware or VM. If so, which hypervisor: kvm, xen etc. 

### Multi processors boot

In case of multiple processor cores, one of the processor is designated as Bootstrap Processor (BSP). It runs the firmware, reset vector, starts kernel. All other cores AP (Application Processor) start later. 
### Microcode patching 

x86 instructions are interface contract. Internally they get translated into microcode by the decoder, from read only array on CPU die. Microcode internals are proprietary stuff. 

Microcodes can be patched, for eg, in case of vulnerabilities like spectre, meltdown etc. You load the patch onto the RAM array first (ROM array are out of touch). When decoder decodes, it'll check the RAM array, and if entry is found, it'll use that. 

Patches can be done at two places:
- Firmware update automatically takes care of this. 
- OS patch at early boot, primary channel for end users without updating the firmware. 

Each physical core has to be patched separately. The patch is prepended to initramfs file. 

```
initramfs = [uncompressed cpio microcode blob] + [compressed cpio rootfs]
```

It has to be loaded early in the boot (to prevent attacks), at the time when there's no filesystem available. It uses a neat trick of reading the patch prepended to initramfs, available from the boot loader at `boot_params.hdr.ramdisk_img`. 

It can also be loaded later by:

```
echo 1 > /sys/devices/system/cpu/microcode/reload
```

but it's risky. 

## Sources
- https://www.0xkato.xyz/linux-boot/
- https://docs.kernel.org/arch/x86/microcode.html
- https://internals-for-interns.com/posts/linux-kernel-startup/
## Related
- [wake-on-lan](/networking/wake-on-lan.md)
- [grub](/os-install/grub.md)
- [initrd](/os-install/initrd.md)
- [anaconda](/os-install/anaconda.md)