# EcoSAP: Python Library for Ecoacoustic Analysis

EcoSAP is a versatile Python library designed for ecoacoustic data processing and analysis. The name "EcoSAP" stands for **Eco**acoustic **S**ound **A**nalysis **P**ython library. It provides a set of powerful modules to facilitate various aspects of ecoacoustic research, including visualization, automatic rain detection, sound processing, and soundscape characterization.


## Modules

### 1. EcoVis

The `EcoVis` module offers an easy-to-use visualization toolkit to explore and represent ecoacoustic data. It provides functions for generating insightful plots, spectrograms, and time-domain visualizations, enabling researchers to gain valuable insights from the acoustic recordings.

### 2. RainDetect

The `RainDetect` module is an automatic rain detector tailored for ecoacoustic recordings. It employs advanced algorithms to identify and flag periods of rainfall within the acoustic data, helping researchers account for weather-induced noise in their analysis.

### 3. EcoProc

The `EcoProc` module is the heart of EcoSAP, providing a comprehensive suite of eco-focused algorithms for sound preprocessing and feature extraction. It optimizes the acoustic data, removing noise, filtering frequencies, and extracting essential features for subsequent analysis.

### 4. EcoFeatures

The `EcoFeatures` module enables extraction of various ecoacoustic features from the data. It includes functions to detect species vocalizations, measure biodiversity indices, and assess soundscape complexity.

### 5. EcoUtils

The `EcoUtils` module provides convenient functions for file manipulation and basic utilities. It allows users to load, save, and handle ecoacoustic data files effortlessly. This module also includes common utility functions for data transformation and general ecoacoustic data management.



## Installation

To install EcoSAP, simply use `pip`:

```bash
pip install ecosap

```


## Usage

```python
# Import the modules
import ecosap.ecovis as ecovis
import ecosap.raindetect as raindetect
import ecosap.ecoproc as ecoproc
import ecosap.ecochar as ecofeatures

# Load your ecoacoustic data
data = load_ecoacoustic_data()

# Visualize the data
EcoVis.plot_spectrogram(data)

# Detect rain periods
rain_periods = RainDetect.detect_rain(data)

# Preprocess the data
processed_data = EcoProc.preprocess(data)

# Characterize the soundscape
species_identification = EcoChar.detect_species(data)
biodiversity_index = EcoChar.calculate_biodiversity(data)

```

## Documentation

For more detailed information and examples, please refer to the [documentation](https://ecosap-library-docs.com).

## Contributing

We welcome contributions! If you find any issues or have ideas for improvements, please submit a pull request or open an issue on the [GitHub repository](https://github.com/davidluna-fn/ecosap).

## License

EcoSAP is released under the [MIT License](https://opensource.org/licenses/MIT).

## About the Author

EcoSAP is proudly developed and maintained by David Luna. Connect with me on [LinkedIn](https://www.linkedin.com/in/davidlunafn/), [Twitter](https://twitter.com/davidlunafn), and via email at davidluna.fn@gmail.com.
