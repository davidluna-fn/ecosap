from sklearn.base import BaseEstimator
from pathlib import Path
from tqdm import tqdm
import torchaudio
import pandas as pd
import torchaudio.functional as F
from scipy.signal import welch, csd


class SpectralComparison(BaseEstimator):
    """
        Get PSD and CSD  from a folder of wav files

        Parameters
        ----------
        subsample : bool, optional
            If True, resample the audio to the sample_rate, by default False
        sample_rate : int, optional
            Sample rate to resample the audio, by default 16000
    """

    def __init__(self, subsample: bool = False, sample_rate: int = 16000):
        self.subsample = subsample
        self.sample_rate = sample_rate

    def fit(self):
        pass

    def transform(self, xpaths: list, ypaths: list):
        """
            Get PSD from a folder of wav files

            Parameters
            ----------
            xpaths : list
                List of paths to wav files
            ypaths : list
                List of paths to wav files

            Returns
            -------
            metrics : pd.
                DataFrame with PSDs
            f
                Frequency vector
        """

        if len(xpaths) != len(ypaths):
            raise ValueError('xpaths and ypaths must have the same length')

        metrics = []
        for xpath, ypath in zip(xpaths, ypaths):
            x, srx = torchaudio.load(xpath)
            y, sry = torchaudio.load(ypath)

            if x.shape[0] > 1:
                x = x.mean(0)
            if y.shape[0] > 1:
                y = y.mean(0)

            if self.subsample:
                if srx != self.sample_rate:
                    x = F.resample(x, srx, self.sample_rate)
                    srx = self.sample_rate
                if sry != self.sample_rate:
                    y = F.resample(y, sry, self.sample_rate)
                    sry = self.sample_rate

            f, sxx = welch(x, fs=srx, nperseg=512, noverlap=0)
            f, syy = welch(y, fs=sry, nperseg=512, noverlap=0)
            f, sxy = csd(x, y, fs=srx, nperseg=512, noverlap=0)

            metrics.append({
                'sxx': sxx,
                'syy': syy,
                'sxy': sxy
            })

        return pd.DataFrame(metrics), f
