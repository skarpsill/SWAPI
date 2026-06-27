---
title: "Insert Mate Load Reference Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Mate_Load_Reference_Example_VB.htm"
---

# Insert Mate Load Reference Example (VBA)

This example shows how to insert a mate load reference.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Gets the mate where to add a load reference.
' 3. Selects a supplemental face for the load reference.
' 4. Inserts a mate load reference.
' 5. Examine the Immediate window.
'
' NOTE: Because the assembly document is used elsewhere, do
' not save changes.
'-------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssemblyDoc As SldWorks.AssemblyDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swMate As SldWorks.Mate2
Dim swMateLoadRef As SldWorks.MateLoadReference
Dim swFeat As SldWorks.Feature
Dim swComponent As SldWorks.Component2
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the assembly document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wrench.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssemblyDoc = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    'Get the mate where to add the load reference
    status = swModelDocExt.SelectByID2("Concentric4", "MATE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swMate = swFeat.GetSpecificFeature2
```

```
    'Insert the load reference using the selected mate and supplemental face
    status = swModelDocExt.SelectByID2("", "FACE", 0.087090587167495, -5.24931403344908E-03, 4.83048001655106E-03, True, 0, Nothing, 0)
    Set swMateLoadRef = swAssemblyDoc.InsertLoadReference(swMate)
```

```
    Debug.Print "Name of load reference added to " & swFeat.Name & " mate = " & swMateLoadRef.Name
    Debug.Print "Number of supplemental faces of the mate load reference for Component1 = " & swMateLoadRef.GetFacesCount(0)
    Set swComponent = swMateLoadRef.Component(0)
    Debug.Print "Name of Component1 = " & swComponent.Name2
```

```
End Sub
```
