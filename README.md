# Modeling_of_APUF_Compositions

Python Code and dataset for APUF and its Compositions

## Getting Started
Below details will provide you instructions for understaning the directory and get it running on your machine for reproducibility.

### Prerequisites

What things you need to install the software and how to install them

```
python 2.7
tensorflow 1.5.0 ( CPU )
Keras 2.1.5
```

### Folder structure

The CRP dataset has been collected for 64 bit and 128 bit challenges. The Example Folder structure from root directory (Main) is given below.
```
Main
|-- 128bit
|   |-- 1Million
|   |   |-- 5-XOR
|   |   |   |-- 5-xor_apuf_128.py
|   |   |-- I-PUF_4_3
|   |   |   |-- ipuf_4_3_128.py
|   |   |-- I-PUF_4_4
|   |   |   |-- ipuf_4_4_128.py
|   |   |-- all_responses
|   |   |   |-- <indivisual apuf responses>
|   |   |-- dataset
|   |   |   |-- <Parity Vector Challenge files>
|   |-- HalfMillion
|   |   |-- 4-XOR
|   |   |   |-- 5-xor_apuf_128.py
|   |   |-- 3-XOR
|   |   |   |-- 5-xor_apuf_128.py
|   |   |-- 2-XOR
|   |   |   |-- 5-xor_apuf_128.py
|   |   |-- APUF
|   |   |   |-- 5-xor_apuf_128.py
|   |   |-- M-PUF
|   |   |   |-- mpuf_128.py
|   |   |-- CM-PUF
|   |   |   |-- cmpuf_128.py
|   |   |-- RM-PUF
|   |   |   |-- rmpuf_128.py
|   |   |-- LS-PUF
|   |   |   |-- lspuf_3
|   |   |   |   |-- lspuf_3_128.py
|   |   |   |-- lspuf_4
|   |   |   |   |-- lspuf_4_128.py
|   |   |-- I-PUF_3_3
|   |   |   |-- ipuf_3_3_128.py
|   |   |-- all_responses
|   |   |   |-- <indivisual apuf responses>
|   |   |-- dataset
|   |   |   |-- <Parity Vector Challenge files>
  
  
|-- 64bit
|   |-- 1Million
|   |   |-- 6-XOR
|   |   |   |-- 6-xor_apuf_64.py
|   |   |-- LS-PUF
|   |   |   |-- lspuf_6
|   |   |   |   |-- lspuf_6_64.py
|   |   |-- I-PUF_3_3
|   |   |   |-- ipuf_3_3_64.py
|   |   |-- I-PUF_3_4
|   |   |   |-- ipuf_3_4_64.py
|   |   |-- I-PUF_4_3
|   |   |   |-- ipuf_4_3_64.py
|   |   |-- I-PUF_4_4
|   |   |   |-- ipuf_4_4_64.py
|   |   |-- all_responses
|   |   |   |-- <indivisual apuf responses>
|   |   |-- dataset
|   |   |   |-- <Parity Vector Challenge files>  
|   |-- HalfMillion
|   |   |-- 2-XOR
|   |   |   |-- 2-xor_apuf_64.py
|   |   |-- 3-XOR
|   |   |   |-- 3-xor_apuf_64.py
|   |   |-- 4-XOR
|   |   |   |-- 4-xor_apuf_64.py
|   |   |-- 5-XOR
|   |   |   |-- 5-xor_apuf_64.py
|   |   |-- LS-PUF
|   |   |   |-- lspuf_3
|   |   |   |   |-- lspuf_3_64.py
|   |   |   |-- lspuf_4
|   |   |   |   |-- lspuf_4_64.py
|   |   |   |-- lspuf_5
|   |   |   |   |-- lspuf_5_64.py
|   |   |-- I-PUF_3_3
|   |   |   |-- ipuf_3_3_64.py
|   |   |-- I-PUF_3_4
|   |   |   |-- ipuf_3_4_64.py
|   |   |-- I-PUF_4_3
|   |   |   |-- ipuf_4_3_64.py
|   |   |-- I-PUF_4_4
|   |   |   |-- ipuf_4_4_64.py
|   |   |-- all_responses
|   |   |   |-- <indivisual apuf responses>
|   |   |-- dataset
|   |   |   |-- <Parity Vector Challenge files>  

```

## Running the tests

For running the tests, go to the respective PUF folder

python <filename>.py


## Authors

* **Pranesh Santikellur** - [Praneshss](https://github.com/Praneshss) Email: [(pranesh.sklr@iitkgp.ac.in)]
* **Aritra Bhattacharyay** - Email: [(aritrab97@gmail.com )]
* **Rajat Subhra Chakraborty** - Email: [(rschakraborty@cse.iitkgp.ernet.in )]

## Citation Code
