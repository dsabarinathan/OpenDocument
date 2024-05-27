# OpenDocument

<p align="center">
  <img src="https://github.com/dsabarinathan/OpenDoc/blob/master/logo/open-document-analysis-high-resolution-logo-transparent%20(1).png" alt="Logo" width="200">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/language-python-blue.svg" alt="Python">
</p>

**OpenDocument: Real-time document processing libraries**

OpenDocument is an open-source project that provides robust and efficient libraries for real-time document image processing. Our goal is to simplify the process of extracting meaningful information from scanned documents through various image preprocessing techniques. Whether you need to enhance image quality, reduce noise, correct skew, or extract text using OCR, OpenDoc offers a comprehensive suite of tools to meet your document processing needs.

In this repository, we share modules and scripts to help you seamlessly process and analyze document images, making OpenDoc a valuable resource for developers, researchers, and anyone working with scanned documents.

## Document Image Preprocessing Modules

Here are some of the features provided by our document image preprocessing modules:

- **Document Image Binarization**:
  Our package efficiently converts grayscale or color images into binary images, enhancing processing and OCR accuracy. Featuring Sauvola adaptive thresholding, it dynamically adjusts thresholds based on local pixel intensities, ensuring precise binarization even with varying lighting and contrast. This improves text extraction in real-time applications like digital archiving and automated data entry. Optimized for performance, the package supports real-time processing on various platforms, handling historical documents, business forms, and more. Key features include adaptive thresholding, enhanced OCR accuracy, real-time processing, and support for grayscale and color images. Achieve superior binarization results with our package.

  
<p align="center">
  <img src="https://github.com/dsabarinathan/OpenDocument/blob/master/example/sample_output_binary.png" alt="Logo" width="500">
</p>

- **Remove Lines**:

  Our package offers effective methods for removing horizontal and vertical lines from document images, improving readability and data extraction. Using advanced image processing techniques, it accurately detects and eliminates lines without affecting the underlying text or graphical elements. This process enhances the clarity of scanned documents, making them more suitable for OCR (Optical Character Recognition) and other automated processing tasks. Ideal for cleaning up forms, tables, and structured documents, our package ensures that lines are removed seamlessly, preserving the integrity of the original content and facilitating more accurate and efficient data analysis.

<p align="center">
  <img src="https://github.com/dsabarinathan/OpenDocument/blob/master/example/lines_removed.png" alt="Logo" width="500">
</p>

- 
- **Image Enhancement**: Improve the quality of scanned documents through various image enhancement techniques.
- **Noise Reduction**: Remove noise from document images to make text and other elements clearer.
- **Skew Correction**: Automatically detect and correct the skew in scanned document images.
- **Segmentation**: Segment document images into text, images, and other components for targeted processing.
- **Optical Character Recognition (OCR)**: Extract text from document images using OCR technology.
- **Feature Extraction**: Extract various features from document images for further analysis.

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
