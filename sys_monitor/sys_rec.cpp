#include <iostream>
#include <Windows.h>
#include <Psapi.h>

// Set your threshold values
const double CPU_THRESHOLD = 80.0;    // Example: 80% CPU usage
const double MEMORY_THRESHOLD = 80.0; // Example: 80% memory usage
const double DISK_THRESHOLD = 80.0;   // Example: 80% disk usage

// Function to get CPU usage
double get_cpu_usage() {
    PDH_FMT_COUNTERVALUE counterValue;
    PDH_HCOUNTER hCounter;

    PdhOpenQuery(nullptr, 0, &hQuery);
    PdhAddCounter(hQuery, L"\\Processor(_Total)\\% Processor Time", 0, &hCounter);
    PdhCollectQueryData(hQuery);
    PdhGetFormattedCounterValue(hCounter, PDH_FMT_DOUBLE, nullptr, &counterValue);

    return counterValue.doubleValue;
}

// Function to get memory usage
double get_memory_usage() {
    MEMORYSTATUSEX memInfo;
    memInfo.dwLength = sizeof(MEMORYSTATUSEX);
    GlobalMemoryStatusEx(&memInfo);

    return static_cast<double>(memInfo.dwMemoryLoad);
}

// Function to get disk space usage
double get_disk_usage() {
    ULARGE_INTEGER freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;
    GetDiskFreeSpaceEx(L"C:", &freeBytesAvailable, &totalNumberOfBytes, &totalNumberOfFreeBytes);

    return (1.0 - static_cast<double>(freeBytesAvailable.QuadPart) / totalNumberOfBytes.QuadPart) * 100.0;
}

// Function to show desktop notification
void show_notification(const wchar_t* title, const wchar_t* message) {
    MessageBox(nullptr, message, title, MB_ICONWARNING);
}

// Main function
int main() {
    double cpu_usage = get_cpu_usage();
    double memory_usage = get_memory_usage();
    double disk_usage = get_disk_usage();

    if (cpu_usage > CPU_THRESHOLD) {
        std::wcout << L"High CPU usage: " << cpu_usage << L"%" << std::endl;
        show_notification(L"High CPU Usage", L"CPU usage is high.");
    }

    if (memory_usage > MEMORY_THRESHOLD) {
        std::wcout << L"High Memory usage: " << memory_usage << L"%" << std::endl;
        show_notification(L"High Memory Usage", L"Memory usage is high.");
    }

    if (disk_usage > DISK_THRESHOLD) {
        std::wcout << L"High Disk usage: " << disk_usage << L"%" << std::endl;
        show_notification(L"High Disk Usage", L"Disk usage is high.");
    }

    std::wcout << L"System check completed." << std::endl;

    return 0;
}
