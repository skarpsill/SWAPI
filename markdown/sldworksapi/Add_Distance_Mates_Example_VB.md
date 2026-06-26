---
title: "Add Distance Mates Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Distance_Mates_Example_VB.htm"
---

# Add Distance Mates Example (VBA)

This example shows how to add distance mate to an assembly.

```
'---------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\assem20.sldasm.
'
' Postconditions:
' 1. Selects Front Plane of the block20<1> component. Click OK to
'    to close the message box.
' 2. Selects Front Plane of the cylinder20<1> component. Click OK
'    to close the message box.
' 3. Adds a distance mate using the Front Plane of each component.
' 4. Displays the number of mates created. Click OK to close the
'    message box.
' 5. Expand Mates in the FeatureManager design tree and examine
'    the graphics area to verify steps 3 and 4.
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swAssy As SldWorks.AssemblyDoc
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim longstatus As Long
Dim mateFeature As Object
Dim mateSelMark As Long
Dim numberOfMatesCreated As Long
Dim status As Boolean
Dim strMessage As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swAssy = swApp.ActiveDoc
    Set swModel = swAssy
    Set swModelDocExt = swModel.Extension
    mateSelMark = 1
    numberOfMatesCreated = 0
```

```
    ' Insert distance mate
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Front Plane@block20-1@assem20", "PLANE", 0, 0, 0, True, mateSelMark, Nothing, swSelectOption_e.swSelectOptionDefault)
    If status Then MsgBox "Front Plane@block20-1@assem20 selected!"
    status = swModelDocExt.SelectByID2("Front Plane@cylinder20-1@assem20", "PLANE", 0, 0, 0, True, mateSelMark, Nothing, swSelectOption_e.swSelectOptionDefault)
    If status Then MsgBox "Front Plane@cylinder20-1@assem20 selected!"
    Set mateFeature = swAssy.AddMate5(swMateType_e.swMateDISTANCE, swMateAlign_e.swMateAlignALIGNED, True, 0.254, 0.254, 0.254, 0.0254, 0.0254, 0, 0.5235987755983, 0.5235987755983, False, False, 0, longstatus)
    If mateFeature Is Nothing Then
       MsgBox "Distance mate failed! "
    Else
       numberOfMatesCreated = numberOfMatesCreated + 1
    End If
```

```
    swModel.ClearSelection2 True
```

```
    strMessage = "Number of mates created = "
    strMessage = strMessage + CStr(numberOfMatesCreated)
    MsgBox strMessage
```

```
    swModel.EditRebuild3
```

```
End Sub
```
