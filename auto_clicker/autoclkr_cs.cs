using System;
using System.Threading;
using System.Windows.Forms;

namespace AutoClickerApp
{
    public partial class MainForm : Form
    {
        private bool pause = true;
        private bool running = true;
        private int delay = 1000;  // milliseconds

        public MainForm()
        {
            InitializeComponent();
            InitializeUI();
        }

        private void InitializeUI()
        {
            Text = "Auto Clicker";

            var startButton = new Button
            {
                Text = "Start / Pause",
                Location = new System.Drawing.Point(10, 10)
            };
            startButton.Click += (sender, e) =>
            {
                pause = !pause;
                LogMessage(pause ? "< Pause >" : "< Start >");
                if (!pause)
                {
                    ThreadPool.QueueUserWorkItem(ClickPeriodically);
                }
            };

            var exitButton = new Button
            {
                Text = "Exit",
                Location = new System.Drawing.Point(120, 10)
            };
            exitButton.Click += (sender, e) =>
            {
                running = false;
                LogMessage("< Exit >");
                Close();
            };

            Controls.Add(startButton);
            Controls.Add(exitButton);

            LogMessage("Press F1 to Start/Pause and Esc to Exit");
        }

        private void LogMessage(string message)
        {
            Console.WriteLine(message);
        }

        private void ClickPeriodically(object state)
        {
            while (running)
            {
                if (!pause)
                {
                    // Simulate mouse click here
                    LogMessage("Clicking...");
                    Thread.Sleep(delay);
                }
            }
        }
    }

    class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
