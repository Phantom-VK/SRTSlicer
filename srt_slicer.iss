[Setup]
AppName=SRT Slicer
AppVersion=1.0
DefaultDirName={pf}\SRT Slicer
DefaultGroupName=SRT Slicer
OutputBaseFilename=SRT_Slicer_Installer
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\SRTSlicer.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\SRT Slicer"; Filename: "{app}\SRTSlicer.exe"
Name: "{userdesktop}\SRT Slicer"; Filename: "{app}\SRTSlicer.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"
