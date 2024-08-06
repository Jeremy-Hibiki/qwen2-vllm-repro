```bash
$ sha256sum /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4/*.safetensors
771294e76d5d7ce91b7d27d0d6326167d4b688e9c1d19992e1c9dba615c1d425  /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4/model-00001-of-00002.safetensors
02dfdb576e8199285b3a0140509c89b3a4b59d808fd388688e8b429c2e80734d  /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4/model-00002-of-00002.safetensors
```

## Deploy with vLLM 0.5.4

### Chat

#### vLLM + GPTQ 4bit + FP8 Cache

```bash
$ typer vllm-offline-demo.py run chat --fp8-cache --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4 "Tell me something about Hu
ggingFace."
```

> Hugging Face is a technology company that that provides a suite of open-source natural language processing (NLP models and tools. These models and tools are used for various tasks such as language translation understanding, text generation, sentiment analysis, and more. The company was founded in 20 by a group of researchers from the French AI institute, called "Presses Universitaires de France". They created a platform called "Transformers" which is a library of pre-trained models machine models for natural language processing tasks. The company also also provides a platform for the machine learning community community to share and collaborate on models models models models models models models models models model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model model

#### vLLM + GPTQ 4bit + FP16 Cache

```bash
$ typer vllm-offline-demo.py run chat --no-fp8-cache --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4 "Tell me something about
 HuggingFace."
```

> Hugging Face is a company and a community that focuses on the development and advancement of natural language processing (NLP) and other AI technologies. It was founded in 2018 by a group of researchers and engineers who were passionate about making AI more accessible and user-friendly. The company is known for its open-source library, Hugging Face Transformers, which provides state-of-the-art natural language processing models and tools for the development of AI applications.
>
> Hugging Face's mission is to democratize AI by making it easier for developers, researchers, and businesses to access and utilize advanced AI technologies. The company offers a range of products and services, including:
>
> 1. **Hugging Face Transformers**: This is a popular open-source library that provides pre-trained models for various NLP tasks, such as text classification, named entity recognition, and question answering. The library supports multiple programming languages and frameworks, making it accessible to a wide range of developers.
>
> 2. **Marian**: A neural machine translation library that offers high-quality translations using pre-trained models.
>
> 3. **Optimum**: A library that optimizes the performance of AI models for deployment on various hardware platforms, including CPUs, GPUs, and TPUs.
>
> 4. **Hugging Face Datasets**: A platform for sharing and discovering datasets used in NLP research and development.
>
> 5. **Hugging Face Spaces**: A platform for sharing and publishing AI models, projects, and research.
>
> 6. **Hugging Face Hub**: A cloud-based platform for training, deploying, and managing AI models, which includes features like version control, collaboration, and model hosting.
>
> 7. **Hugging Face AI**: A suite of AI services for businesses, including custom model training, integration, and deployment.
>
> Hugging Face has also been instrumental in fostering a community of AI enthusiasts and practitioners through its forums, workshops, and events, which help in sharing knowledge, collaborating on projects, and advancing the field of AI.

#### HF Transformers + GPTQ 4bit

```bash
$ typer transformers-demo.py run --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4 "Tell me something about HuggingFace."
```

> Hugging Face is a company and an open-source platform that provides tools, models, and resources for the development of natural language processing (NLP) applications. It was founded in 2018 by a group of researchers who wanted to make it easier for developers and researchers to share and use pre-trained machine learning models for NLP tasks.
>
> The Hugging Face platform offers a wide range of pre-trained models in various languages and domains, such as sentiment analysis, question answering, text generation, and more. These models are trained on large datasets and can be fine-tuned for specific tasks with minimal effort. The platform also includes a model hub where users can easily download and use these models in their projects.
>
> Hugging Face's mission is to democratize AI by making it accessible to everyone, from beginners to experienced professionals. They provide tutorials, documentation, and forums to help users get started with AI and NLP. Additionally, they offer a suite of tools like Transformers, which is a powerful library for building state-of-the-art NLP models using pre-trained models, and Datasets, which allows users to easily load and preprocess data for their models.
>
> Hugging Face has gained significant popularity in the AI community due to its user-friendly approach and the high-quality models it provides. It has become a go-to resource for many developers and researchers working on NLP projects.

### Summary

Sample text is from https://patents.google.com/patent/kr102166913b1/en

#### w/o fp8 cache:

```bash
$ typer vllm-offline-demo.py run summary --no-fp8-cache --lang zh --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4
```

> 这段文本描述了一种自偏置缓冲器电路及其在存储器设备中的应用。自偏置缓冲器电路包括缓冲单元和偏置调整单元。缓冲单元基于参考电压提供自偏置电压，根据该自偏置电压驱动，并比较输入信号与参考电压以生成输出信号。偏置调整单元根据参考电压提升自偏置电压。
>
> 具体来说，偏置调整单元可以包括响应于参考电压开启的增强型晶体管，用于提升自偏置电压。偏置调整单元可以进一步包括在电源使能信号的反转信号下控制其操作的功率 MOS 晶体管和/或接地 MOS 晶体管，以确保在电源电压和接地电压之间稳定地提供自偏置电压。
>
> 缓冲单元可以包括差分单元，用于基于参考信号和输入信号生成自偏置电压和输出信号，以及偏置单元，用于根据自偏置电压驱动差分单元。差分单元可以包括参考单元和输入/输出单元，其中参考单元提供自偏置电压，输入/输出单元生成输出信号。
>
> 偏置调整单元可以包括功率单元和接地单元，用于在参考电压高于或等于启动电压时提升自偏置电压。当参考电压低于或等于启动电压时，偏置调整单元可以对自偏置电压进行对称调整。
>
> 存储器设备包括存储核心、自偏置缓冲器电路和控制单元。存储核心存储或输出数据，自偏置缓冲器电路接收存储核心的数据或向存储核心传输外部数据，响应于控制信号。控制单元生成控制信号以控制存储核心和自偏置缓冲器电路。
>
> 自偏置缓冲器电路可以用于提高存储器设备的运行速度和可靠性，通过使用适合操作特性的自偏置电压来增加操作速度和可靠性。通过调整自偏置电压，可以确保自偏置缓冲器电路在参考电压为 VDD/2 时对称工作，从而选择最宽的数据获取窗口的参考电压 VDD/2 作为自偏置电压的参考电压，以提高存储器设备的运行速度。
>
> 此外，自偏置缓冲器电路可以应用于各种数字系统，其中使用存储器设备以提高系统的运行速度。

```bash
$ typer vllm-offline-demo.py run summary --no-fp8-cache --lang en --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4
```

> The text describes a self-bias buffer circuit and a memory device including the same, which are designed to improve the operation speed and reliability of semiconductor devices.
>
> The self-bias buffer circuit includes a buffer unit that provides a self-bias voltage based on a reference voltage, and a bias adjustment unit that boosts this self-bias voltage. The buffer unit compares an input signal with the reference voltage to generate an output signal, while the bias adjustment unit ensures the buffer operates efficiently across different reference voltage levels.
>
> The bias adjustment unit can be implemented using boost transistors that turn on in response to the reference voltage to boost the self-bias voltage. The buffer unit can be further divided into a reference unit and an input/output unit, with the reference unit providing the self-bias voltage and the input/output unit generating the output signal.
>
> The memory device incorporating this self-bias buffer circuit can store and output data more efficiently, with improved setup and hold times for data latching. The self-bias buffer circuit is designed to operate symmetrically based on a reference voltage level, allowing the memory controller to select an optimal reference voltage for maximum performance.
>
> Overall, the self-bias buffer circuit and memory device aim to enhance the performance of semiconductor devices by optimizing the self-bias voltage and improving data handling capabilities.

#### w/ fp8 cache:

```bash
$ typer vllm-offline-demo.py run summary --fp8-cache --lang zh --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4
```

> 这段描述描述描述一种自偏偏置缓冲器缓冲器电路电路，并 to improve 一种自偏偏的置缓冲的的电路。该。，该一种自偏偏偏的的当缓冲的的。.。该一种自偏偏偏偏偏的的缓冲缓冲的的。....一种自偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏偏

```bash
$ typer vllm-offline-demo.py run summary --fp8-cache --lang en --model-name /data/GPT/models/Qwen2-7B-Instruct-GPTQ-Int4
```

> The text disc describes describes to provide a self self to the the the the the to the the to the the to the the to the the to the the to the the to the to the to the to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be to be
