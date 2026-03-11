# Career Roadmap: Computer Architecture & Power-Performance Modeling

This guide provides a structured, end-to-end plan to become an expert in **Computer Architecture** and **Power-Performance Modeling** — skills that are central to roles at CPU/GPU companies (Intel, AMD, ARM, NVIDIA, Qualcomm, Apple Silicon), cloud providers (Google, Microsoft, Meta), and academic research labs.

This repository's work on PUF modeling, deep learning attacks, and challenge-response pair (CRP) analysis overlaps directly with hardware characterization, circuit-level behavior, and performance/security trade-offs — a strong foundation to build upon.

---

## Table of Contents

1. [Role Overview](#1-role-overview)
2. [Skills Map](#2-skills-map)
3. [Phase 1 — Foundations (Months 1–3)](#phase-1--foundations-months-13)
4. [Phase 2 — Core Computer Architecture (Months 4–7)](#phase-2--core-computer-architecture-months-47)
5. [Phase 3 — Power & Performance Modeling (Months 8–11)](#phase-3--power--performance-modeling-months-811)
6. [Phase 4 — Advanced Topics & Research (Months 12–18)](#phase-4--advanced-topics--research-months-1218)
7. [Essential Tools & Simulators](#7-essential-tools--simulators)
8. [Benchmark Suites](#8-benchmark-suites)
9. [Hands-On Projects](#9-hands-on-projects)
10. [Connection to This Repository](#10-connection-to-this-repository)
11. [Interview Preparation](#11-interview-preparation)
12. [Reference Books & Papers](#12-reference-books--papers)

---

## 1. Role Overview

| Role | What You Do | Key Skills |
|------|-------------|------------|
| **CPU/GPU Architect** | Design ISA, microarchitecture, pipelines | RTL, uarch modeling, performance simulation |
| **Performance Modeling Engineer** | Build analytical and simulation models of processors | gem5, cycle-accurate simulators, workload analysis |
| **Power Modeling Engineer** | Estimate dynamic/static power at chip, block, and system level | McPAT, CACTI, SPICE, RTL power analysis |
| **Platform Performance Engineer** | Optimize software-hardware co-design for products | Profiling, benchmarking, DVFS, thermal modeling |
| **Hardware Security Researcher** | Analyze hardware vulnerabilities (PUF attacks, side-channels) | PUF modeling, ML attacks, silicon characterization |

---

## 2. Skills Map

```
Computer Architecture & Power-Performance Modeling
│
├── Digital Logic & VLSI Fundamentals
│   ├── Boolean algebra, gates, flip-flops
│   ├── CMOS transistor operation
│   └── Timing analysis, setup/hold constraints
│
├── Computer Architecture
│   ├── Instruction Set Architecture (ISA)
│   ├── Pipelining & Hazard Handling
│   ├── Superscalar & Out-of-Order Execution
│   ├── Branch Prediction
│   ├── Memory Hierarchy (Caches, TLB, DRAM)
│   ├── Interconnects & I/O
│   └── Multi-core & NUMA Architectures
│
├── Power Modeling
│   ├── Dynamic Power (C·V²·f·α)
│   ├── Static Power (Leakage)
│   ├── McPAT / CACTI Power Models
│   ├── DVFS (Dynamic Voltage and Frequency Scaling)
│   └── Thermal Modeling
│
├── Performance Modeling
│   ├── Analytical Models (Amdahl, Roofline)
│   ├── Cycle-Accurate Simulation (gem5, Sniper, ZSim)
│   ├── Statistical / Sampling Techniques
│   ├── Performance Counter Analysis (PMU, perf, VTune)
│   └── Workload Characterization
│
├── Hardware Security (this repository)
│   ├── Physical Unclonable Functions (PUFs)
│   ├── Side-Channel Attacks (power, timing, EM)
│   ├── ML-based PUF Modeling Attacks
│   └── Secure Hardware Design
│
└── Software & Tools
    ├── C/C++, Python, SystemVerilog/VHDL
    ├── gem5, McPAT, CACTI, Sniper, ZSim
    ├── SPEC CPU, TPC, MLPerf benchmarks
    └── Linux perf, Intel VTune, ARM Streamline
```

---

## Phase 1 — Foundations (Months 1–3)

### Month 1: Digital Logic & Computer Organization

**Topics:**
- Number systems, Boolean algebra, logic gates
- Combinational circuits: multiplexers, adders, decoders
- Sequential circuits: flip-flops, registers, FSMs
- CMOS basics: transistor operation, static and dynamic logic

**Resources:**
- 📖 *Digital Design and Computer Architecture* — Harris & Harris (Chapter 1–5)
- 📖 *Fundamentals of Digital Logic with VHDL Design* — Brown & Vranesic
- 🎓 [nand2tetris](https://www.nand2tetris.org/) — build a computer from first principles (free online course)
- 🎓 MIT OCW 6.004 — Computation Structures

**Practice:**
- Implement combinational and sequential circuits on paper and in simulation
- Use Logisim or Digital (free tools) to simulate circuits

---

### Month 2: Computer Organization

**Topics:**
- Von Neumann architecture, fetch-decode-execute cycle
- ALU design and datapath
- Single-cycle and multi-cycle processor design
- MIPS / RISC-V ISA basics
- Assembly programming

**Resources:**
- 📖 *Computer Organization and Design: RISC-V Edition* — Patterson & Hennessy (Chapters 1–4)
- 🎓 Berkeley CS61C — Great Ideas in Computer Architecture ([free lectures on YouTube](https://www.youtube.com/@berkeley-cs61c))
- 🎓 [RISC-V ISA Spec](https://riscv.org/technical/specifications/)

**Practice:**
- Write RISC-V assembly programs
- Simulate a single-cycle MIPS processor in a hardware description language

---

### Month 3: Operating Systems & System Software Basics

**Topics:**
- Process and memory management
- Virtual memory and address translation
- System calls and OS-hardware interaction
- How compilers map high-level code to hardware

**Resources:**
- 📖 *Operating Systems: Three Easy Pieces* — Arpaci-Dusseau (free at [ostep.org](https://ostep.org/))
- 📖 *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CS:APP, Chapters 1–6)
- 🎓 CMU 15-213 — Introduction to Computer Systems

**Practice:**
- Use `perf stat` on Linux to collect hardware performance counters
- Analyze cache behavior with `valgrind --tool=cachegrind`

---

## Phase 2 — Core Computer Architecture (Months 4–7)

### Month 4: Pipelining & Instruction-Level Parallelism (ILP)

**Topics:**
- 5-stage pipeline (IF, ID, EX, MEM, WB)
- Data hazards: stalls, forwarding, interlocking
- Control hazards: branch prediction, speculative execution
- Structural hazards
- Performance metrics: CPI, IPC, throughput

**Resources:**
- 📖 *Computer Organization and Design* — Patterson & Hennessy (Chapter 4)
- 📖 *Computer Architecture: A Quantitative Approach* — Hennessy & Patterson (Appendix C)
- 🎓 Georgia Tech CS 6290 — High Performance Computer Architecture ([Udacity](https://www.udacity.com/course/high-performance-computer-architecture--ud007))

**Practice:**
- Implement a pipelined MIPS/RISC-V processor in Verilog/SystemVerilog
- Calculate CPI for instruction traces with different stall scenarios

---

### Month 5: Out-of-Order Execution & Superscalar Processors

**Topics:**
- Tomasulo algorithm, reservation stations
- Reorder buffer (ROB), register renaming
- In-order vs out-of-order processors
- Superscalar issue, decode width
- Modern processors: ARM Cortex-A, Intel Core, AMD Zen microarchitecture

**Resources:**
- 📖 *Computer Architecture: A Quantitative Approach* — Hennessy & Patterson (Chapter 3)
- 📄 [Agner Fog's Microarchitecture Guide](https://www.agner.org/optimize/microarchitecture.pdf)
- 📄 Intel, AMD, and ARM architecture optimization manuals (free PDFs)
- 🎓 David Wentzlaff's Computer Architecture (Princeton) on Coursera

**Practice:**
- Trace through Tomasulo algorithm examples
- Read Intel Software Developer Manual Chapters on microarchitecture

---

### Month 6: Memory Hierarchy

**Topics:**
- Cache organization: direct-mapped, set-associative, fully associative
- Cache replacement policies: LRU, FIFO, random
- Cache coherence (MESI protocol)
- Virtual memory, TLBs, page tables
- DRAM: SDRAM, DDR, memory controllers
- Prefetching strategies

**Resources:**
- 📖 *Computer Architecture: A Quantitative Approach* — Hennessy & Patterson (Chapter 2)
- 📖 CACTI Manual and documentation
- 📄 *What Every Programmer Should Know About Memory* — Ulrich Drepper ([free PDF](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf))
- 🎓 CMU 18-447 — Introduction to Computer Architecture

**Practice:**
- Model cache hit/miss rates for example access patterns
- Run CACTI to model cache access time and energy

---

### Month 7: Parallel & Multi-Core Architecture

**Topics:**
- Multi-core processor design
- Symmetric vs asymmetric multiprocessing
- Cache hierarchy in multi-core (L1/L2/L3 shared vs private)
- Memory consistency models (TSO, relaxed)
- GPU architecture overview (SIMT, warp scheduling)
- NUMA architectures

**Resources:**
- 📖 *A Primer on Memory Consistency and Cache Coherence* — Sorin, Hill & Wood (available via [Synthesis Lectures on Computer Architecture](https://link.springer.com/book/10.1007/978-3-031-01733-0))
- 📖 *Programming Massively Parallel Processors* — Kirk & Hwu
- 🎓 MIT 6.823 — Computer System Architecture
- 📄 NVIDIA CUDA C Programming Guide

**Practice:**
- Write OpenMP/pthreads programs and analyze scalability
- Profile GPU kernels with NVIDIA Nsight

---

## Phase 3 — Power & Performance Modeling (Months 8–11)

### Month 8: Power Consumption Fundamentals

**Topics:**
- CMOS power components: dynamic, short-circuit, leakage
- Dynamic power: `P = α·C·V²·f` (activity factor, capacitance, voltage, frequency)
- Static power: subthreshold leakage, gate oxide tunneling
- Power-performance trade-offs
- Technology scaling and power density (dark silicon)
- Voltage islands, clock gating, power gating

**Resources:**
- 📖 *CMOS VLSI Design* — Weste & Harris (Chapters on power)
- 📄 McPAT Paper: *"McPAT: An Integrated Power, Area, and Timing Modeling Framework"* — Li et al. (MICRO 2009)
- 📄 *"Dark Silicon and the End of Multicore Scaling"* — Esmaeilzadeh et al. (ISCA 2011)
- 🎓 Stanford EE 271 — Introduction to VLSI Systems

---

### Month 9: Analytical Performance Models

**Topics:**
- Roofline model (compute vs memory bandwidth bound)
- Amdahl's Law and scalability limits
- Little's Law in memory systems
- Queuing models for performance analysis
- Memory-level parallelism (MLP)
- Effective bandwidth measurement

**Resources:**
- 📄 *"Roofline: An Insightful Visual Performance Model"* — Williams et al. (Communications of ACM, 2009)
- 📄 *"Bounding the Effect of Partition Crossings"* — Eyerman & Eeckhout
- 🎓 Berkeley CS 267 — Applications of Parallel Computers
- 🛠️ [Intel Advisor Roofline Analysis](https://www.intel.com/content/www/us/en/developer/tools/oneapi/advisor.html)

**Practice:**
- Apply the Roofline model to DGEMM, FFT, and sparse matrix-vector multiply
- Compute arithmetic intensity for different code patterns

---

### Month 10: Cycle-Accurate Simulation with gem5

**Topics:**
- gem5 architecture: SimObject, event-driven simulation
- CPU models: AtomicSimpleCPU, TimingSimpleCPU, O3CPU (out-of-order)
- Memory system: cache hierarchy, memory controllers
- Full system vs syscall emulation mode
- Configuring and running simulations
- Parsing gem5 statistics

**Resources:**
- 🌐 [gem5 official website and documentation](https://www.gem5.org/)
- 📄 *"The gem5 Simulator"* — Binkert et al. (SIGARCH 2011)
- 🎓 gem5 Tutorial at ISCA/HPCA (slides on gem5.org)
- 📺 gem5 bootcamp videos (YouTube)

**Practice:**
```bash
# Install gem5
git clone https://gem5.googlesource.com/public/gem5
cd gem5
scons build/X86/gem5.opt -j$(nproc)

# Run a simple simulation
./build/X86/gem5.opt configs/example/se.py \
  --cmd=tests/test-progs/hello/bin/x86/linux/hello

# Run with a specific CPU model
./build/X86/gem5.opt configs/example/se.py \
  --cmd=<your_benchmark> --cpu-type=O3CPU \
  --caches --l2cache --l1d_size=32kB --l1i_size=32kB --l2_size=256kB
```

---

### Month 11: McPAT & CACTI for Power-Area Modeling

**Topics:**
- McPAT: modeling processor power, area, and timing
- CACTI: cache and memory access time, energy, area
- Integrating gem5 with McPAT (gem5-to-mcpat scripts)
- Per-component breakdown: core, cache, NoC, DRAM
- Validating models against real silicon measurements

**Resources:**
- 🌐 [McPAT source code](https://github.com/HewlettPackard/mcpat)
- 🌐 [CACTI source code](https://github.com/HewlettPackard/cacti)
- 📄 *"CACTI 6.0: A Tool to Understand Large Caches"* — Muralimanohar et al.
- 📄 *"Revisiting McPAT"* — Xi et al. (discussion of model accuracy)

**Practice:**
```bash
# Clone and build McPAT
git clone https://github.com/HewlettPackard/mcpat
cd mcpat && make

# Run with an example config
./mcpat -infile ProcessorDescriptionFiles/Xeon.xml -print_level 5

# Run CACTI for cache modeling
cd cacti && make
echo "65536 32 8 1 1 1 1 1 1 45 0 0 0 0 0 1 0 1 1 1 1 1 0" | ./cacti
```

---

## Phase 4 — Advanced Topics & Research (Months 12–18)

### Month 12–13: Hardware Security & PUF Modeling (This Repository's Domain)

**Topics:**
- Physical Unclonable Functions (PUFs): how silicon variation creates unique fingerprints
- Arbiter PUF operation and its challenge-response mechanism
- PUF compositions: XOR-PUF, iPUF, LS-PUF, M-PUF
- ML-based modeling attacks: LR, SVM, neural networks
- This repository's approach: DFFNN attacks on APUF compositions
- Side-channel attacks: power analysis, timing attacks, EM emissions
- Countermeasures: obfuscation, noise injection, error-correcting codes

**Resources:**
- 📄 This repository's corresponding paper: *"Deep Learning based Model Building Attacks on Arbiter PUF Compositions"* — Santikellur et al. (ePrint 2019/566)
- 📄 *"A Large Scale Characterization of RO-PUF"* — Hori et al.
- 📄 *"Modeling Attacks on Physical Unclonable Functions"* — Rührmair et al.
- 📖 *Introduction to Hardware Security and Trust* — Tehranipoor & Wang
- 📄 *"The Interpose PUF"* — Nguyen et al. (CHES 2019)

**Connecting This Repo to Power-Performance:**
Power consumption signatures directly enable PUF attacks. Your experience with ML-based CRP modeling here maps directly to:
- Statistical power modeling (predicting circuit behavior from measurements)
- Hardware characterization techniques
- Correlating measurable signals (timing delay, power) to internal state

---

### Month 14–15: Accelerator Architecture

**Topics:**
- Domain-Specific Architectures (DSAs): TPU, NPU, Inferentia
- Systolic array design for matrix multiplication
- Dataflow architectures (weight-stationary, input-stationary, output-stationary)
- Neural network inference hardware
- Near-memory and in-memory computing
- FPGA-based acceleration

**Resources:**
- 📄 *"In-Datacenter Performance Analysis of a Tensor Processing Unit"* — Jouppi et al. (ISCA 2017)
- 📄 *"Eyeriss: An Energy-Efficient Reconfigurable Accelerator for DNNs"* — Chen et al. (JSSC 2017)
- 📖 *Computer Architecture: A Quantitative Approach* — Hennessy & Patterson (Chapter 7, DNN Accelerators)
- 🎓 MIT 6.825 / Stanford CS 217 — Hardware Accelerators for Machine Learning

---

### Month 16–17: Advanced Power Management

**Topics:**
- DVFS: voltage-frequency scaling algorithms and hardware
- Power delivery network (PDN) design
- Thermal management: throttling, heat sink design
- Power capping and power budgets in data centers
- Race-to-sleep vs race-to-halt strategies
- Energy proportionality in servers

**Resources:**
- 📄 *"Managing the Impact of Increasing Memory Capacity on Machines"* — various Intel whitepapers
- 📄 AMD/ARM/Intel power management architecture guides
- 📄 *"Power Management in the Intel Core Microarchitecture"* — Intel Hotchips presentation

---

### Month 18: Research & Contribution

**Topics:**
- Reading and reviewing top conference papers (ISCA, MICRO, HPCA, ASPLOS, DAC)
- Reproducing results from published papers
- Contributing to open-source simulator projects (gem5, CACTI)
- Writing technical reports and publishing

**Key Conferences:**
| Conference | Focus |
|-----------|-------|
| ISCA | International Symposium on Computer Architecture |
| MICRO | IEEE/ACM International Symposium on Microarchitecture |
| HPCA | International Symposium on High-Performance Computer Architecture |
| ASPLOS | Architectural Support for Programming Languages and Operating Systems |
| DAC | Design Automation Conference |
| CHES | Cryptographic Hardware and Embedded Systems (hardware security) |

---

## 7. Essential Tools & Simulators

### Cycle-Accurate Simulators

| Tool | Type | Language | Use Case |
|------|------|----------|----------|
| **gem5** | Cycle-accurate | C++ | Full system, CPU + memory simulation |
| **Sniper** | Interval simulation | C++ | Fast multi-core simulation |
| **ZSim** | Cycle-approximate | C++ | Very fast multi-core |
| **MARSSx86** | Cycle-accurate | C++ | x86 full system |
| **ChampSim** | Trace-driven | C++ | Branch predictor / prefetcher research |

### Power & Area Modeling

| Tool | Purpose | Input |
|------|---------|-------|
| **McPAT** | Processor power/area/timing | XML config + gem5 stats |
| **CACTI** | Cache/memory power/area | Parameter file |
| **Wattch** | Cycle-level power | Modified SimpleScalar |
| **Jouletrack** | Mobile power estimation | Workload characteristics |
| **Synopsys PrimeTime PX** | RTL power (industry) | Gate-level netlist + switching activity |

### Performance Analysis (Host Machine)

| Tool | Platform | Use |
|------|----------|-----|
| `perf` | Linux | Hardware performance counters |
| Intel VTune | Linux/Windows | Detailed CPU profiling |
| ARM Streamline | ARM | Multi-core profiling |
| NVIDIA Nsight | GPU | GPU performance analysis |
| AMD uProf | AMD CPUs | CPU profiling |
| `cachegrind` | Linux | Cache simulation |
| `likwid` | Linux | Performance counters, energy (RAPL) |

### RTL & Circuit Simulation

| Tool | Use |
|------|-----|
| Verilog/SystemVerilog | RTL design |
| ModelSim / Questa | RTL simulation |
| Cadence Virtuoso | Analog/SPICE simulation |
| Synopsys Design Compiler | Logic synthesis |
| Yosys + OpenROAD | Open-source synthesis/PnR |

---

## 8. Benchmark Suites

| Suite | Domain | Use |
|-------|--------|-----|
| **SPEC CPU2017** | Single-core CPU | Industry-standard CPU benchmarking |
| **PARSEC** | Multi-core | Parallel workload characterization |
| **NAS Parallel Benchmarks** | HPC | Supercomputing workloads |
| **MLPerf** | ML inference/training | AI hardware benchmarking |
| **STREAM** | Memory bandwidth | Memory subsystem stress testing |
| **Rodinia** | GPU/GPGPU | Parallel computing |
| **TPC-H/TPC-C** | Database | Database server benchmarking |
| **LINPACK** | HPC | Floating-point compute |

---

## 9. Hands-On Projects

### Beginner Projects
1. **Implement a 5-stage MIPS pipeline in Verilog** — handle data/control hazards
2. **Cache simulator in Python** — simulate hit/miss rates for LRU/FIFO/random policies
3. **Branch predictor comparison** — implement 1-bit, 2-bit, correlating, and tournament predictors
4. **RISC-V emulator in C** — implement all base integer instructions

### Intermediate Projects
5. **Run gem5 with O3CPU and compare with SimpleCPU** — analyze IPC, cache miss rates
6. **Run McPAT on gem5 output** — produce per-component power breakdown for a benchmark
7. **Roofline analysis on a matrix multiply kernel** — measure arithmetic intensity and peak performance
8. **PUF modeling extension (this repo)** — extend existing DFFNN attacks with dropout/regularization

### Advanced Projects
9. **gem5 + McPAT pipeline** — automate running SPEC benchmarks, collecting gem5 stats, feeding to McPAT
10. **DVFS simulator** — model how voltage/frequency choices affect performance and energy
11. **Custom cache prefetcher in gem5** — implement and evaluate stride or stream prefetcher
12. **Hardware side-channel attack** — use RAPL energy counters to detect PUF response patterns

---

## 10. Connection to This Repository

Your work on this APUF modeling repository is directly applicable to power-performance roles in several ways:

### Machine Learning for Hardware Characterization
The DFFNN attack models in this repo demonstrate:
- **Statistical hardware modeling**: predicting circuit outputs from input patterns — the same skill used for modeling processor performance from microarchitectural events
- **Feature engineering for hardware**: parity vectors as features for ML models map to how performance analysts create feature sets from performance counter data

### PUF Behavior as a Power Model Analogy
PUF delay differences arise from manufacturing process variation — the same variability that determines:
- Within-chip power variation across cores
- Leakage current differences between transistors
- Thermal hotspot formation

### Building on This Work
Concrete extensions you can pursue:
1. **Power side-channel analysis**: measure power traces during PUF evaluation; use the ML models from this repo to classify responses from power traces
2. **Timing analysis**: model delay distributions across PUF instances; relate to setup-time violations and processor timing margins
3. **Neural network hardware mapping**: implement the DFFNN from this repo on a hardware accelerator; measure energy/throughput trade-offs

---

## 11. Interview Preparation

### Common Topics for Computer Architecture Roles

**Cache & Memory:**
- How does a set-associative cache work?
- What is the MESI cache coherence protocol?
- Calculate cache miss rate and AMAT for a given access pattern
- What causes TLB misses? How are they handled?

**Pipelining:**
- How does forwarding handle data hazards?
- What is the difference between RAW, WAW, and WAR hazards?
- How does speculative execution improve IPC?
- How does Meltdown/Spectre exploit speculative execution? *(links to this repo's security theme)*

**Power:**
- What is the difference between dynamic and static power?
- How does DVFS save energy?
- What is dark silicon? What are solutions?
- How does clock gating reduce power?

**Design Trade-offs:**
- Why don't we simply increase clock frequency for better performance?
- What are the trade-offs between cache size and access latency?
- When is out-of-order execution better/worse than in-order?

### Practice Platforms
- [Leetcode — Computer Architecture tag](https://leetcode.com/)
- [Glassdoor — AMD/Intel/ARM interview questions]
- [GeeksForGeeks — Computer Organization & Architecture section](https://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/)
- Past exam problems from MIT 6.004, CMU 18-447, Berkeley CS 61C

---

## 12. Reference Books & Papers

### Core Textbooks

| Book | Authors | Best For |
|------|---------|----------|
| *Computer Organization and Design: RISC-V Edition* | Patterson & Hennessy | Foundational architecture |
| *Computer Architecture: A Quantitative Approach* (6th ed.) | Hennessy & Patterson | Advanced architecture |
| *Digital Design and Computer Architecture* | Harris & Harris | Digital logic to processor design |
| *Computer Systems: A Programmer's Perspective* (CS:APP) | Bryant & O'Hallaron | System-level programming |
| *CMOS VLSI Design: A Circuits and Systems Perspective* | Weste & Harris | VLSI design and power |
| *Modern Processor Design* | Shen & Lipasti | Superscalar architectures |
| *Introduction to Hardware Security and Trust* | Tehranipoor & Wang | Hardware security (connects to this repo) |

### Landmark Papers

| Paper | Where | Why Important |
|-------|-------|--------------|
| "Roofline: An Insightful Visual Performance Model" | ACM CACM 2009 | Foundation of performance analysis |
| "McPAT: An Integrated Power, Area, and Timing Modeling Framework" | MICRO 2009 | Standard power modeling tool |
| "The gem5 Simulator" | SIGARCH 2011 | Standard simulation platform |
| "In-Datacenter Performance Analysis of a TPU" | ISCA 2017 | Modern accelerator design |
| "Eyeriss: An Energy-Efficient Reconfigurable Accelerator" | JSSC 2017 | DNN accelerator energy modeling |
| "Dark Silicon and the End of Multicore Scaling" | ISCA 2011 | Power wall problem |
| "Deep Learning based Model Building Attacks on APUF" | ePrint 2019/566 | **This repository's paper** |

### Online Resources

- 🌐 [Agner Fog's optimization manuals](https://www.agner.org/optimize/) — CPU microarchitecture details
- 🌐 [gem5.org](https://www.gem5.org/) — simulator documentation and tutorials
- 🌐 [WikiChip](https://en.wikichip.org/) — processor microarchitecture deep dives
- 🌐 [Chips and Cheese](https://chipsandcheese.com/) — modern CPU microarchitecture analysis
- 🌐 [Real World Tech](https://www.realworldtech.com/) — processor architecture analysis
- 🌐 [Anandtech](https://www.anandtech.com/) — processor benchmarks and architecture reviews
- 🌐 [IACR ePrint](https://eprint.iacr.org/) — hardware security papers (including this repo's paper)

---

## Summary Timeline

| Period | Focus | Key Deliverable |
|--------|-------|----------------|
| Months 1–3 | Foundations | Complete nand2tetris, RISC-V assembly programs |
| Months 4–7 | Core Architecture | Implement pipelined processor in Verilog |
| Months 8–11 | Power & Performance | gem5 + McPAT simulation pipeline |
| Months 12–15 | Advanced Topics | Accelerator architecture project |
| Months 16–18 | Research | Paper reproduction, conference submission |

---

*This roadmap was created as part of the [Modeling of APUF Compositions](https://github.com/Praneshss/Modeling_of_APUF_Compositions) repository to help researchers transition from hardware security modeling to broader computer architecture and power-performance engineering roles.*
