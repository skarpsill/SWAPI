---
title: "Rename Component and Update References Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rename_Component_and_Update_References_Example_VB.htm"
---

# Rename Component and Update References Example (VBA)

This example shows how to rename a component and update its references.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Copy and paste Main into your project.
' 2. Insert a class module and copy and paste Class1 into that module.
' 3. Copy public_documents\samples\tutorial\EDraw\claw to c:\test\claw.
' 4. Open c:\test\claw\claw-mechanism.sldasm and save the file as
'    claw-mechanism-copy.sldasm.
' 5. Close claw-mechanism-copy.sldasm and reopen claw-mechanism.sldasm.
' 6. Open the Immediate window.
'
' Postconditions:
' 1. Renames the center component to centerXXX.
' 2. Fires the RenameItemNotify event.
' 3. Saves the assembly.
' 4. Fires the RenamedDocumentNotify event.
' 5. Updates references.
' 6. Examine the FeatureManager design tree and Immediate window.
' 7. Close claw-mechanism.sldasm and open
'    c:\test\claw\claw-mechanism-copy.sldasm to verify that the
'    center component was renamed to centerXXX.
'---------------------------------------------------------------------
'Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssy As SldWorks.AssemblyDoc
Dim swAssyEvents As Class1
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swAssy = swApp.ActiveDoc
```

```
    'Set up event
    Set swAssyEvents = New Class1
    Set swAssyEvents.swAssy = swApp.ActiveDoc
```

```
    Set swModel = swAssy
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("center-1@claw-mechanism", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    errors = swModelDocExt.RenameDocument("centerXXX")
    swModelDocExt.Rebuild swRebuildOptions_e.swRebuildAll
    status = swModel.Save3(swSaveAsOptions_e.swSaveAsOptions_Silent + swSaveAsOptions_e.swSaveAsOptions_SaveReferenced, errors, warnings)
```

```
End Sub
```

```
'Class1
Option Explicit

Public WithEvents swAssy As SldWorks.AssemblyDoc

'Fire notification when item is renamed
Public Function swAssy_RenameItemNotify(ByVal entType As Long, ByVal oldName As String, ByVal newName As String) As Long
	Debug.Print "RenameItemNotify fired"
End Function

'Fire notification for Rename Documents dialog
Public Function swAssy_RenamedDocumentNotify(ByRef swObj As Object) As Long
	Dim swRenamedDocumentReferences As SldWorks.RenamedDocumentReferences
	Dim searchPaths As Variant
	Dim pathNames As Variant
	Dim i As Long
	Dim nbr As Long

	Set swRenamedDocumentReferences = swObj

	swRenamedDocumentReferences.UpdateWhereUsedReferences = True
	swRenamedDocumentReferences.IncludeFileLocations = True

	searchPaths = swRenamedDocumentReferences.GetSearchPath
	nbr = UBound(searchPaths)
	Debug.Print "Search paths:"
	For i = 0 To nbr
	Debug.Print (" " & searchPaths(i))
	Next i

	swRenamedDocumentReferences.Search

	pathNames = swRenamedDocumentReferences.ReferencesArray
	nbr = UBound(pathNames)
	Debug.Print "References:"
	For i = 0 To nbr
	Debug.Print (" " & pathNames(i))
	Next i

	swRenamedDocumentReferences.CompletionAction = swRenamedDocumentFinalAction_e.swRenamedDocumentFinalAction_Ok

	Debug.Print "RenamedDocumentNotify fired"

End Function
```
