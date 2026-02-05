; LRU Tracker - Inno Setup Installer Script
; Creates a professional Windows installer with GUI

#define MyAppName "LRU Tracker"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "FC Operations"
#define MyAppExeName "LRU_Tracker.exe"
#define MyAppAssocName MyAppName + " Data File"
#define MyAppAssocExt ".json"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
AppId={{E8F9A2B4-3C5D-4E6F-8A9B-1C2D3E4F5A6B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=..\distribution\packages
OutputBaseFilename=LRU_Tracker_Setup
SetupIconFile=..\distribution\lru_icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\distribution\INSTALL_WINDOWS.txt"; DestDir: "{app}"; DestName: "README.txt"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{app}\lru_data.json.backup"

[Code]
var
  DataDirPage: TInputDirWizardPage;

procedure InitializeWizard;
begin
  { Create custom page for data directory }
  DataDirPage := CreateInputDirPage(wpSelectDir,
    'Select Data Folder', 'Where should LRU Tracker save your data?',
    'Your LRU tracking data will be saved here. This folder will NOT be deleted during uninstall.',
    False, '');
  DataDirPage.Add('');
  DataDirPage.Values[0] := ExpandConstant('{userdocs}\LRU Tracker Data');
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  Result := True;
  if CurPageID = DataDirPage.ID then
  begin
    { Create data directory }
    ForceDirectories(DataDirPage.Values[0]);
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  DataDir: String;
  ConfigFile: String;
begin
  if CurStep = ssPostInstall then
  begin
    { Save data directory location to config }
    DataDir := DataDirPage.Values[0];
    ConfigFile := ExpandConstant('{app}\data_location.txt');
    SaveStringToFile(ConfigFile, DataDir, False);
  end;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
  DataDir: String;
  ConfigFile: String;
begin
  if CurUninstallStep = usUninstall then
  begin
    { Ask if user wants to keep data }
    if MsgBox('Do you want to keep your LRU tracking data?' + #13#10 + 
              'Select YES to keep your data for future installations.' + #13#10 +
              'Select NO to delete all data.', 
              mbConfirmation, MB_YESNO) = IDYES then
    begin
      { Keep the data directory }
      ConfigFile := ExpandConstant('{app}\data_location.txt');
      if LoadStringFromFile(ConfigFile, DataDir) then
      begin
        MsgBox('Your data has been preserved at:' + #13#10 + DataDir, mbInformation, MB_OK);
      end;
    end
    else
    begin
      { Delete data if user chose NO }
      ConfigFile := ExpandConstant('{app}\data_location.txt');
      if LoadStringFromFile(ConfigFile, DataDir) then
      begin
        DelTree(DataDir, True, True, True);
      end;
    end;
  end;
end;
