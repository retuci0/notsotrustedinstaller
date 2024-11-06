# parameter for the executable name
param (
    [string]$executableName
)

# requires to be run as admin
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    $scriptPath = $MyInvocation.MyCommand.Path
    Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`"" -Verb RunAs
    exit
}

# install ntobjectmanager if it's not installed already
if (-not (Get-Module -ListAvailable -Name NtObjectManager)) {
    Install-Module -Name NtObjectManager -Force -Scope CurrentUser
}

# start the desired process as a child of trustedinstaller to gain its privileges
Start-Service -Name TrustedInstaller
$parent = Get-NtProcess -ServiceName TrustedInstaller
$proc = New-Win32Process $executableName -CreationFlags NewConsole -ParentProcess $parent

# run whoami /groups to verify you're running as ti
# it should say somewhere NT SERVICE\TrustedInstaller
# if you just run whoami it will say nt authority/system
# because SYSTEM is the actual user and TrustedInstaller is just
# a set of privileges that the SYSTEM account can have