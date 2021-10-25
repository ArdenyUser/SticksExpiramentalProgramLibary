echo SDK COMPILER...
cd C:\DEVwindows\
mkdir C:\DEVwindows\CompiledOutput
python SDKcompiler.py
Rename-Item -Path "C:\DEVwindows\CompiledOutput\Exelinker.config" -NewName "Exelinker.ps1"
Invoke-ps2exe .\Exelinker.ps1 .\RunProgram.exe
C:\DEVwindows\cpile.ps1
