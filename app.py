import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QFileDialog, 
                             QCheckBox, QComboBox, QTextEdit, QSpinBox, QDoubleSpinBox, QProgressBar)
from PyQt5.QtCore import Qt, QProcess
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QDialog, QScrollArea, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Help")
        self.setGeometry(200, 200, 1200, 900)

        # Create a scrollable area for the help text
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(10, 10, 480, 380)

        help_text = """
       <p><b style='color:#D91656;'>1. Sync Window (sw):</b> Defines the window size in seconds for video synchronization. Larger Sync Window size results in more effective computation.</p>
            <p><b style='color:#D91656;'>2. Sync Start Time (ss):</b> The point in time from which the analysis begins. The default range is between 0 and 1.</p>
            <p><b style='color:#D91656;'>3. Frame Rate (fps):</b> Specifies the frame rate for video processing. Default is 30 fps. For higher bitrate videos, prefer using 60 fps.</p>
            <p><b style='color:#D91656;'>4. Model (HD, 4K):</b> Defines the VMAF model for video quality assessment.</p>
            <p><b style='color:#D91656;'>5. Threads:</b> Number of threads to use for computation. Max thread count = CPU thread count.</p>
            <p><b style='color:#D91656;'>6. Subsampling:</b> Refers to the number of samples taken from the signal, decreasing the amount of data being processed. Recommended subsample value is 1.</p>
            <p><b style='color:#D91656;'>7. Verbose:</b> Enables detailed logging for troubleshooting.</p>
            <p><b style='color:#D91656;'>8. Reverse Sync:</b> Syncs using the reference video first frames with the distorted video.</p>
            <p><b style='color:#D91656;'>9. CAMBI Heatmap:</b> Visualizes motion blur and contrast variations.</p>
            <p><b style='color:#D91656;'>10. End Sync:</b> Ends processing when the shortest video ends.</p>
            <p><b style='color:#D91656;'>11. Sync Only:</b> Measures sync offset without calculating VMAF.</p>
            <p><b style='color:#D91656;'>12. Denoise:</b> Applies denoising (removes noise) to the distorted video.</p>
            <p><b style='color:#D91656;'>13. Brightness:</b> Adjusts the brightness of the distorted video.</p>
            <br>
            <p><b style='color:#D91656;'> The recommended values for good comparison:</b></p>
            <p><b style='color:#D91656;'> Sync Window: </b> 1 to 10 frames </p>
            <p><b style='color:#D91656;'> Sync Start Time: </b> 0 to 1 second </p>
            <p><b style='color:#D91656;'> Frame Rate: </b> 30 fps (Standard)</p>
            <p><b style='color:#D91656;'> Subsampling: </b> 1 (no subsampling) </p>
            <br>
            <p><b style='color:#D91656;'> The Video Quality Metrics:</b></p>
            <p><b style='color:#D91656;'> VMAF: </b> A perceptual quality score that predicts how viewers perceive the quality of video, considering various visual features.</p>
            <p><b style='color:#D91656;'> PSNR: </b> A metric that measures the peak signal-to-noise ratio between two videos, indicating their level of similarity.</p>
            <p><b style='color:#D91656;'> SSIM: </b> A measure of structural similarity between two images or videos, focusing on luminance, contrast, and structure.</p>
            <!-- <p><b style='color:#D91656;'> MSAD: </b> A metric that calculates the average absolute pixel differences between two images or videos.</p> -->
            <!-- <p><b style='color:#D91656;'> MSE: </b> A metric that calculates the average squared differences between the pixel values of two images or videos.</p> -->
            <!-- <p><b style='color:#D91656;'> DELTA: </b> Measures the perceptual difference in color and texture between the reference and distorted video.</p> -->
            <!-- <p><b style='color:#D91656;'> DMOS: </b> A subjective metric that approximates perceived video quality, often used as a basis for human assessment.</p> -->
            <!-- <p><b style='color:#D91656;'> NQI: </b> A normalized quality index that evaluates the perceptual quality by combining features like contrast and texture similarity.</p> -->
            <br>
            <br>
            <table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">
            <thead>
            <tr>
                <th style="padding: 8px; background-color: #D91656; color: white;">Metric</th>
                <th style="padding: 8px; background-color: #D91656; color: white;">Optimal Range</th>
                <th style="padding: 8px; background-color: #D91656; color: white;">Ideal Value</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td style="padding: 8px;">VMAF</td>
                <td style="padding: 8px;">0-100</td>
                <td style="padding: 8px;">100</td>
            </tr>
            <tr>
                <td style="padding: 8px;">PSNR</td>
                <td style="padding: 8px;">&gt;40 dB</td>
                <td style="padding: 8px;">&gt;50 dB</td>
            </tr>
            <tr>
                <td style="padding: 8px;">SSIM</td>
                <td style="padding: 8px;">0-1</td>
                <td style="padding: 8px;">1.0</td>
            </tr>
            <!--
            <tr>
                <td style="padding: 8px;">MSAD</td>
                <td style="padding: 8px;">0-&infin;</td>
                <td style="padding: 8px;">0</td>
            </tr>
            <tr>
                <td style="padding: 8px;">MSE</td>
                <td style="padding: 8px;">0-&infin;</td>
                <td style="padding: 8px;">0</td>
            </tr>
            <tr>
                <td style="padding: 8px;">DELTA</td>
                <td style="padding: 8px;">0-&infin;</td>
                <td style="padding: 8px;">0</td>
            </tr>
            <tr>
                <td style="padding: 8px;">DMOS</td>
                <td style="padding: 8px;">0-100</td>
                <td style="padding: 8px;">0</td>
            </tr>
            <tr>
                <td style="padding: 8px;">NQI</td>
                <td style="padding: 8px;">0-1</td>
                <td style="padding: 8px;">1.0</td>
            </tr>
            -->
            </tbody>
            </table>
        """


        help_label = QLabel(help_text)
        help_label.setTextFormat(Qt.RichText)  # Ensures that the HTML content is rendered correctly
        scroll_area.setWidget(help_label)

        
        # Layout for Help dialog
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)
        self.setLayout(layout)

class VMAFApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

    def initUI(self):
        self.setWindowTitle('VMAF Calculator')
        self.setGeometry(100, 100, 600, 800)

        # Set global styles
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;  /* White background for the main widget */
                color: #D91656;  /* Pink-Red color for text */
                font-family: Arial;
                font-size: 14px;
                font-weight: bold;  /* Making all text bold */
            }
            QPushButton {
                background-color: #BFECFF;  /* Soft blue for buttons */
                color: #D91656;  /* Pink-red text color */
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #D91656;  /* Pink-red border */
                font-weight: bold;  /* Making text bold */
            }
            QPushButton:hover {
                background-color: #D91656;  /* Pink-red background on hover */
                color: #FFFFFF;  /* White text on hover */
            }
            QLineEdit, QDoubleSpinBox, QSpinBox, QComboBox {
                background-color: #FFFFFF;  /* White background for inputs */
                color: #D91656;  /* Pink-red text color */
                border: 1px solid #D91656;  /* Pink-red border for inputs */
                padding: 4px;
                border-radius: 5px;
                font-weight: bold;  /* Making text bold */
            }
            QLineEdit:focus, QDoubleSpinBox:focus, QSpinBox:focus, QComboBox:focus {
                border: 1px solid #78B3CE;  /* Soft blue border when focused */
            }
            QLabel {
                color:#78B3CE;  
                font-size: 15px;
                font-weight: bold;  /* Making text bold */
            }
            QTextEdit {
                background-color: #FFFFFF;  /* White background for text area */
                color: #D91656;  /* Pink-red text color */
                border: 1px solid #D91656;  /* Pink-red border */
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;  /* Making text bold */
            }
            QCheckBox {
                color: #D91656;  /* Pink-red color for checkboxes */
                font-weight: bold;  /* Making text bold */ 
            }
            QComboBox QAbstractItemView {
                background-color: #FFFFFF;  /* White background for dropdown */
                color: #D91656;  /* Pink-red text color for dropdown items */
                border: 1px solid #D91656;  /* Pink-red border */
                font-weight: bold;  /* Making text bold */
            }
            QComboBox::drop-down {
                border: none;  /* Removes the border from the dropdown arrow */
            }
            QSpinBox::up-button, QDoubleSpinBox:up-button, QDoubleSpinBox:down-button , QSpinBox::down-button {
                background-color: #BFECFF;  /* Soft blue for the up/down buttons */
                border: 1px solid #D91656;  /* Pink-red border */
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover, QDoubleSpinBox:up-button:hover, QDoubleSpinBox:down-button:hover {
                background-color: #D91656;  /* Pink-red on hover */
                color: #FFFFFF;  /* White text on hover */
            }
            QProgressBar {
                background-color: #FFFFFF;  /* White background for the progress bar */
                color: #D91656;  /* Pink-red text color */
                border-radius: 5px;
                border: 1px solid #D91656;  /* Pink-red border */
                font-weight: bold;  /* Making text bold */
            }
            QProgressBar::chunk {
                background-color: #78B3CE;  /* Soft blue for the filled portion */
            }
            QProgressBar:disabled {
                background-color: #D3D3D3;  /* Gray background when disabled */
            }
        """)

        # Main layout for the window
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)  # Reduced padding around the window
        main_layout.setSpacing(5)  # Moderate spacing between widgets

        # Create top layout for logo and help button
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)  # No padding or margins
        top_layout.setSpacing(5)  # Reduced spacing

        # Create logo label
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap("./static/Logo.png")  # Ensure the logo path is correct
        self.logo_pixmap = self.logo_pixmap.scaled(300, 300, Qt.KeepAspectRatio)  # Resize logo to fit
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignLeft)  # Align the logo to the left

        # Create the Help button and position it to the right
        self.help_button = QPushButton("Help")
        self.help_button.clicked.connect(self.show_help)

        # Add logo and help button to the top_layout (logo left, help button right)
        top_layout.addWidget(self.logo_label)
        top_layout.addStretch()  # This pushes the help button to the right
        top_layout.addWidget(self.help_button)

        # Add the top_layout to the main_layout (logo + help button at the top)
        main_layout.addLayout(top_layout)

        # Add the rest of the widgets (inputs, buttons, etc.)
        self.initWidgets(main_layout)

        self.setLayout(main_layout)

    def initWidgets(self, layout):
        # Distorted video input
        self.distorted_label = QLabel('Distorted Video:')
        self.distorted_input = QLineEdit()
        self.distorted_button = QPushButton('Browse')
        self.distorted_button.clicked.connect(self.select_distorted_video)

        layout.addWidget(self.distorted_label)
        layout.addWidget(self.distorted_input)
        layout.addWidget(self.distorted_button)

        # Reference video input
        self.reference_label = QLabel('Reference Video:')
        self.reference_input = QLineEdit()
        self.reference_button = QPushButton('Browse')
        self.reference_button.clicked.connect(self.select_reference_video)

        layout.addWidget(self.reference_label)
        layout.addWidget(self.reference_input)
        layout.addWidget(self.reference_button)

        # Sync Window
        self.sw_input = QDoubleSpinBox()
        self.sw_input.setRange(0, 9999)
        self.sw_input.setSingleStep(0.1)
        self.sw_input.setPrefix('Sync Window (sw): ')
        layout.addWidget(self.sw_input)

        # Sync Start Time
        self.ss_input = QDoubleSpinBox()
        self.ss_input.setRange(0, 9999)
        self.ss_input.setSingleStep(0.1)
        self.ss_input.setPrefix('Sync Start Time (ss): ')
        layout.addWidget(self.ss_input)

        # Frame Rate (fps)
        self.fps_input = QDoubleSpinBox()
        self.fps_input.setRange(0, 240)
        self.fps_input.setSingleStep(1)
        self.fps_input.setPrefix('Frame Rate (fps): ')
        layout.addWidget(self.fps_input)

        # Subsampling
        self.subsample_input = QSpinBox()
        self.subsample_input.setRange(1, 100)
        self.subsample_input.setValue(1)
        self.subsample_input.setPrefix('Subsampling (n): ')
        layout.addWidget(self.subsample_input)

        # Model selection
        self.model_input = QComboBox()
        self.model_input.addItems(["HD", "4K"])
        self.model_input.setToolTip('Select VMAF Model')
        layout.addWidget(self.model_input)

        # Threads
        self.threads_input = QSpinBox()
        self.threads_input.setRange(0, 16)
        self.threads_input.setValue(0)
        self.threads_input.setPrefix('Threads: ')
        layout.addWidget(self.threads_input)

        # Checkboxes for optional flags
        self.reverse_checkbox = QCheckBox('Reverse Sync')
        self.verbose_checkbox = QCheckBox('Verbose')
        self.progress_checkbox = QCheckBox('Progress')
        self.endsync_checkbox = QCheckBox('End Sync')
        self.cambi_checkbox = QCheckBox('CAMBI Heatmap')
        self.sync_only_checkbox = QCheckBox('Sync Only')
        self.denoise_checkbox = QCheckBox('Apply Denoising')

        layout.addWidget(self.reverse_checkbox)
        layout.addWidget(self.verbose_checkbox)
        layout.addWidget(self.progress_checkbox)
        layout.addWidget(self.endsync_checkbox)
        layout.addWidget(self.cambi_checkbox)
        layout.addWidget(self.sync_only_checkbox)
        layout.addWidget(self.denoise_checkbox)

        # Brightness checkbox
        self.brightness_checkbox = QCheckBox('Apply Brightness Adjustment')
        self.brightness_input = QDoubleSpinBox()
        self.brightness_input.setRange(0, 3)
        self.brightness_input.setSingleStep(0.1)
        self.brightness_input.setPrefix('Brightness Factor: ')
        self.brightness_input.setValue(1.0)
        self.brightness_input.setEnabled(False)  # Disable by default

        layout.addWidget(self.brightness_checkbox)
        layout.addWidget(self.brightness_input)

        # Connect checkbox to enable/disable brightness input
        self.brightness_checkbox.toggled.connect(self.brightness_input.setEnabled)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)  # Hidden by default
        layout.addWidget(self.progress_bar)

        # Output display area
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(self.output_display)

        # Compute and Exit buttons
        self.compute_button = QPushButton('Compute VMAF')
        self.compute_button.clicked.connect(self.compute_vmaf)
        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self.close)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.compute_button)
        button_layout.addWidget(self.exit_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        
    def show_help(self):
        # Create and display a Help dialog
        help_dialog = HelpDialog(self)
        help_dialog.exec_()

    def select_distorted_video(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Distorted Video')
        if file:
            self.distorted_input.setText(file)

    def select_reference_video(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Reference Video')
        if file:
            self.reference_input.setText(file)

    def compute_vmaf(self):
        
        # Change button text to "Computing" when the process starts
        self.compute_button.setText('Computing...')  
        self.compute_button.setEnabled(False)  # Disable button to prevent multiple clicks
        
        # Prepare command
        cmd = [
            'python3', 'internal/Vmaf_calculator.py',  # Backend script name
            '-d', self.distorted_input.text(),
            '-r', self.reference_input.text(),
            '-sw', str(self.sw_input.value()),
            '-ss', str(self.ss_input.value()),
            '-fps', str(self.fps_input.value()),
            '-subsample', str(self.subsample_input.value()),
            '-model', self.model_input.currentText(),
            '-threads', str(self.threads_input.value()),
        ]

        # Add flags if checked
        if self.reverse_checkbox.isChecked():
            cmd.append('-reverse')
        if self.verbose_checkbox.isChecked():
            cmd.append('-verbose')
        if self.progress_checkbox.isChecked():
            cmd.append('-progress')
            self.progress_bar.setVisible(True)  # Make progress bar visible
            self.progress_bar.setValue(0)  # Reset progress bar to 0%
            self.progress_bar.setFormat("%p%")  # Display progress percentage
            self.progress_bar.setAlignment(Qt.AlignCenter)  # Center the text inside progress bar
        else:
            self.progress_bar.setVisible(False)  # Hide progress bar if not checked
        if self.endsync_checkbox.isChecked():
            cmd.append('-endsync')
        if self.cambi_checkbox.isChecked():
            cmd.append('-cambi_heatmap')
        if self.sync_only_checkbox.isChecked():
            cmd.append('-sync_only')
        if self.denoise_checkbox.isChecked():
            cmd.append('-denoise')
        
        # Add brightness only if checkbox is checked
        if self.brightness_checkbox.isChecked():
            cmd.append('-brightness')
            cmd.append(str(self.brightness_input.value()))

        print("Executing Command:", ' '.join(cmd))  # For debugging
        
        # Start the process and capture output
        self.output_display.clear()  # Clear previous output
        self.process.start(' '.join(cmd))
        

    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.output_display.append(data)
        self.output_display.verticalScrollBar().setValue(self.output_display.verticalScrollBar().maximum())
        
        # Check if "progress" is in the output
        if "progress" in data:
            try:
                # Try to parse the progress value (e.g., progress = 45.2%)
                progress_value_str = data.split("progress = ")[1].strip().split("%")[0]
                progress_value = float(progress_value_str)  # Convert to a floating point number
                
                # Update progress bar if a valid progress percentage is found
                self.progress_bar.setValue(int(progress_value))  # The progress bar accepts integer values
                
            except (IndexError, ValueError) as e:
                # In case parsing fails, just ignore and do not update progress
                pass  # For debugging, you can log or handle the error if needed


    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.output_display.append(data)
        self.output_display.verticalScrollBar().setValue(self.output_display.verticalScrollBar().maximum())

    def process_finished(self):
        
        # Revert button text to "Compute VMAF" after processing is complete
        self.compute_button.setText('Compute VMAF')  
        self.compute_button.setEnabled(True)  # Re-enable the button
        
        self.output_display.append("VMAF computation finished.")
        self.progress_bar.setValue(100)  # Set progress bar to 100% when finished
        self.output_display.verticalScrollBar().setValue(self.output_display.verticalScrollBar().maximum())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VMAFApp()
    ex.show()
    sys.exit(app.exec_())

