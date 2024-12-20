# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Option to compute frame-by-frame VMAF, PSNR, and SSIM metrics.
- Support for comparing HD and 4K video formats.
- Feature to export VMAF analysis results as a JSON file.

### Changed
- Improved computation speed by optimizing the backend script.
- Added denoising and brightness feature using ffmpeg.
- Added UI for better user experience.

### Deprecated
- No deprecated features yet.

### Removed
- No features removed.

### Fixed
- Addressed an issue where FFmpeg would crash on large 4K videos.
- Fixed incorrect handling of paths with special characters.

### Security
- No security-related changes yet.

---

## [Version 1.1.0] - 2024-10-15

### Added
  **Initial release** of the project with support for:
- Initial release of the VMAF Calculator project.
- Basic functionality to compute VMAF, PSNR, and SSIM between a reference video and a distorted video.
- User interface developed using PyQt5.
- Support for HD and 4K video formats.
- Added denoising and brightness feature using ffmpeg
- Frame-by-frame analysis output in JSON format.'

### Changed
- Refined the UI layout for better user experience.

### Deprecated
- No deprecated features.

### Removed
- None.

### Fixed
- Minor UI glitches when handling large videos.

### Security
- No security-related changes yet.

