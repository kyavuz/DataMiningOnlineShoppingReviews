using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;

namespace DataMiningOnlineShoppingReviews
{
    public partial class DataMiningOnlineShoppingReviews : Form
    {
        private string projectDirectory = AppDomain.CurrentDomain.BaseDirectory;
        private string datasetFileName = "user_reviews.txt"; // dataset
        private string datasetFilePath, getDatasetPythonPath, getSentimentPythonPath, getKeywordPythonPath;

        public DataMiningOnlineShoppingReviews()
        {
            InitializeComponent();
            this.FormClosing += MainForm_FormClosing;
            datasetFilePath = Path.Combine(projectDirectory, datasetFileName);
            getDatasetPythonPath = Path.Combine(projectDirectory, "..\\.." , "getDataset.py");
            getSentimentPythonPath = Path.Combine(projectDirectory, "..\\..", "sentimentAnalysis.py");
            getKeywordPythonPath = Path.Combine(projectDirectory, "..\\..", "keywordAnalysis.py");
        }

        private void SetBusy(bool isBusy)
        {
            // Ekranın "busy" veya "free" durumuna göre görünümünü ayarla
            if (isBusy)
            {
                // Ekranı "busy" durumuna getir
                this.Cursor = Cursors.WaitCursor;
                button1.Enabled = false; // Butonu devre dışı bırakabilirsiniz
                button2.Enabled = false; // Butonu devre dışı bırakabilirsiniz
                button3.Enabled = false; // Butonu devre dışı bırakabilirsiniz
            }
            else
            {
                // Ekranı "free" durumuna getir
                this.Cursor = Cursors.Default;
                button1.Enabled = true; // Butonu tekrar etkinleştir
                button2.Enabled = true; // Butonu tekrar etkinleştir
                button3.Enabled = true; // Butonu tekrar etkinleştir
            }
        }

        private void RunPyCode(object sender, EventArgs e, string arg)
        {
            try
            {
                SetBusy(true);

                string pythonScriptPath = "";
                string task = "";

                // Python betiği için dosya yolu
                if (arg != null)
                {
                    task = arg;
                }
                else
                {
                }

                if (task.Equals("getDataSet"))
                {
                    pythonScriptPath = getDatasetPythonPath;
                }
                else if (task.Equals("sentiment"))
                {
                    pythonScriptPath = getSentimentPythonPath;
                }
                else if (task.Equals("keyword"))
                {
                    pythonScriptPath = getKeywordPythonPath;
                }

                // Python yürütücüsünün yolu
                string pythonInterpreterPath = "C:\\Users\\Kağan Yavuz\\AppData\\Local\\Programs\\Python\\Python312\\python.exe";

                // Python betiği ve argümanları
                string arguments = $"\"{pythonScriptPath}\""; // $"\"{pythonScriptPath}\" arg1 arg2";

                // ProcessStartInfo oluştur
                ProcessStartInfo startInfo = new ProcessStartInfo
                {
                    FileName = pythonInterpreterPath,
                    Arguments = arguments,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                // Process oluştur
                using (Process process = new Process
                {
                    StartInfo = startInfo
                })
                {
                    // Process'i başlat
                    process.Start();

                    // Çıkış ve hata çıktılarını oku
                    string output = process.StandardOutput.ReadToEnd();
                    string error = process.StandardError.ReadToEnd();

                    // Çıkış ve hata çıktılarını kullanarak işlemin durumuyla ilgili işlem yapabilirsiniz
                    if (!string.IsNullOrEmpty(output))
                    {
                        // TextBox'a çıktıyı yazdır
                        textBox2.Text = output;
                    }

                    // Bekle ve ardından kapat
                    process.WaitForExit();

                    if (task.Equals("getDataSet"))
                    {
                        textBox1.Text = "Dataset Collected!";
                    }
                    else if (task.Equals("sentiment"))
                    {
                        textBox1.Text = "Sentiment Analysis Done!";
                    }
                    else if (task.Equals("keyword"))
                    {
                        textBox1.Text = "Keyword Analysis Done!";
                    }

                    SetBusy(false);
                }
            }
            catch (Exception ex)
            {
                SetBusy(false);
                MessageBox.Show($"Hata: {ex.Message}");
            }
        }
        private void GetDatasetButton_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            RunPyCode(sender, e, "getDataSet");
        }

        private void DataMiningOnlineShoppingReviews_Load(object sender, EventArgs e)
        {

        }

        private void SentimentAnalysis_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            RunPyCode(sender, e, "sentiment");
        }

        private void KeywordAnalysis_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            RunPyCode(sender, e, "keyword");
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            // since the "get dataset" button is not working properly, this lines commented out. (we need the dataset)

            //try
            //{
            //    // Dosyayı sil
            //    File.Delete(datasetFilePath); 
            //    MessageBox.Show("Dataset başarıyla silindi.", "Bilgi", MessageBoxButtons.OK, MessageBoxIcon.Information);
            //}
            //catch (Exception ex)
            //{
            //    MessageBox.Show($"Dataset silinirken bir hata oluştu: {ex.Message}", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
            //}
        }
    }
}
