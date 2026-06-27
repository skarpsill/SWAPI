---
title: "Assign Columnset to Folder before Browsing Add-in Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Assign_Columnset_To_Folder_Before_Browsing_Addin_Example_VBNET.htm"
---

# Assign Columnset to Folder before Browsing Add-in Example (VB.NET)

This example shows how to create an add-in that triggers a
pre-browse event and assigns a columnset to a folder before it is browsed.

```vb
  '--------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio as Administrator.
 ' 2. Click File > New > Project > Visual Basic > Class Library (.NET Framework).
 ' 3. Select .NET Framework 4.5 or later in the dropdown.
 ' 4. Type ClassLibrary1 in Name.
 ' 5. Click Browse and navigate to the folder where to create the project.
 ' 6. Click OK.
  ' 7. Right-click the project name in the Solution Explorer and click Add Reference.
 ' 8. In the Add Reference dialog:
 '    a. Add the SOLIDWORKS PDM Professional interop assembly as a reference (click Browse in the
 '       left-side panel, click EPDM.Interop.epdm.dll,
 '       and click OK).
 '    b. Click Close.
  ' 9. Right-click the project name in the Solution Explorer and click Properties.
 '10. In the Properties window:
 '    a. On the Application tab, click Assembly Information.
 '    b. De-select Make assembly COM-Visible.
 '    c. On the Compile tab, select x64 in the Target CPU dropdown, de-select Prefer 32-bit, and select Register for COM interop.
 '11. Save the project.
 '12. Copy the code below to your project's Class1.vb.
 '13. To populate the GUID attribute, click Tools > Create GUID in the IDE,
 '    select GUID Format 6, click Copy, and click Exit. Replace <Guid("")> with
 '    the copied string.
 '14. Open the SOLIDWORKS PDM Professional Administration tool, expand a vault_name node,
 '    and log in as Admin.
 '15. Under vault_name, right-click Add-ins, and click New Add-in.
  '    a. Navigate to the bin directory of your built project.
 '    b. Select ClassLibrary1.dll.
 '    c. Click Open.
 '    d. Click OK.
  '16. Click OK after reading the SOLIDWORKS PDM Professional warning dialog.
 '17. Expand Columns under the vault_name in the Admin Tool.
'18. Right click File List Columns and select  New Column Set.
'19. Change the order of existing columns or add a custom column and name the new column set.
'20. Click  OK.
 '21. Change the ID parameter in SetColumnSetID of the code to match your new column set ID. As none of the other folders and column sets exist, the code will only execute the Case Else section.
'22. Save the project.
'23. Select Release in the Solution Configurations dropdown and x64 in the Solution Platforms dropdown.
 '24. Click Build > Build Solution.
 '
 ' Postconditions:
 ' 1. Open File Explorer on a view of vault_name and log in as Admin.
 ' 2. This add-in triggers a pre-browse event before the root folder is browsed.
' 3. Click OK on each dialog as it appears.
' 4. This add-in registers and loads a user's column set into the root folder before it is browsed.
  '---------------------------------------------------------------------------------------

 Imports EPDM.Interop.epdm
 Imports System.Runtime.InteropServices

 <Guid("")>
 <ComVisible(True)>
```

PublicClassAPIs

ImplementsIEdmAddIn5

PublicvaultAsIEdmVault22

DimppocolumnsetAsEdmColumnSet

DimppocolumnsetsAsEdmColumnSet()

PublicSubGetAddInInfo(ByRefpoInfoAsEdmAddInInfo,ByValpoVaultAsIEdmVault5,ByValpoCmdMgrAsIEdmCmdMgr5)ImplementsIEdmAddIn5.GetAddInInfo

Try

poInfo.mbsAddInName ="VB.NET Add-In"

poInfo.mbsCompany ="Dassault Systemes"

poInfo.mbsDescription ="Responding to folder browse events"

poInfo.mlAddInVersion = Now.ToString("yyyyMMdd")

poInfo.mlRequiredVersionMajor = 29

poInfo.mlRequiredVersionMinor = 0

poCmdMgr.AddHook(EdmCmdType.EdmCmd_PreBrowseFolder)

CatchexAsRuntime.InteropServices.COMException

MsgBox("HRESULT
= 0x"+ ex.ErrorCode.ToString("X")
+ vbCrLf + ex.Message)

CatchexAsException

MsgBox(ex.Message)

EndTry

EndSub

PublicSubOnCmd(ByRefpoCmdAsEdmCmd,ByRefppoDataAsEdmCmdData())ImplementsIEdmAddIn5.OnCmd

DimFolderIDAsInteger

DimAffectedFileAsEdmCmdData

DimIDAsInteger

DimNameAsString

Name =" "

MsgBox("poCmd.meCmdType = "+ poCmd.meCmdType.ToString)

IfpoCmd.meCmdType =
EdmCmdType.EdmCmd_PreBrowseFolderThen

vault = poCmd.mpoVault

Getcolumnsets(ID, Name)

vault. SetColumnSetID (ID)

ForEachAffectedFileInppoData

FolderID = AffectedFile.mlObjectID1

'Set the column set for
the folder to be browsed

SelectCaseFolderID

Case3

'vault.SetColumnSetID(5)

'GetCurrentColumnSet(ID, Name)

'MsgBox("Browsing Folder ID=3")

Case4

'vault.SetColumnSetID(6)

'MsgBox("Browsing Folder ID=4")

Case5

'vault.SetColumnSetID(7)

'GetCurrentColumnSet(ID, Name)

'MsgBox("Browsing Folder ID=5")

Case6

'vault.SetColumnSetID(8)

'MsgBox("Browsing Folder ID=6")

Case7

'vault.SetColumnSetID(9)

'GetCurrentColumnSet(ID,
Name)

'MsgBox("Browsing Folder ID=7")

Case8

'vault.SetColumnSetID(10)

'MsgBox("Browsing Folder ID=8")

CaseElse

GetCurrentColumnSet(ID, Name)

MsgBox("Browsing
Folder ID="+ FolderID.ToString())

EndSelect

Next

EndIf

EndSub

PublicSubGetCurrentColumnSet(ByRefColumnIDAsInteger,ByRefColumnNameAsString)

vault. GetCurrentColumnSet (ppocolumnset)

ColumnName = ppocolumnset. mbsColumnSetName

ColumnID = ppocolumnset. mlColumnSetID

MsgBox("Current column set ID
= "+ ColumnID.ToString +" Current column set name = "+ ColumnName)

EndSub

PublicSubGetcolumnsets(ByRefColumnIDAsInteger,ByRefColumnNameAsString)

vault. GetColumnSets (ppocolumnsets)

DimitemAsEdmColumnSet

ForEachitemInppocolumnsets

ColumnName = item. mbsColumnSetName

ColumnID = item. mlColumnSetID

MsgBox("User's column set ID
= "+ ColumnID.ToString +" User's column set name = "+ ColumnName)

Next

EndSub

EndClass

[Back to top](#top)
