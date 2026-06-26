---
title: "Open Part from Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Part_from_Assembly_Example_VB.htm"
---

# Open Part from Assembly Example (VBA)

This example shows how to open a part document from an assembly document.

```
'---------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select a vertex, face, or an edge of a component.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part document to which the selected vertex,
'    face, or edge belongs.
' 2. Examine the Immediate window and graphics area.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swCompEnt As SldWorks.Entity
    Dim swPartFeat As SldWorks.Feature
    Dim swComp As SldWorks.Component2
    Dim swCompModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swPartEnt As SldWorks.Entity
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swCompModelConfig As Configuration
    Dim nRetval As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    Set swCompEnt = swSelMgr.GetSelectedObject6(1, 0)
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)
    Set swCompModel = swComp.GetModelDoc
    Set swConfigMgr = swCompModel.ConfigurationManager
    Set swCompModelConfig = swConfigMgr.ActiveConfiguration
    Set swModelDocExt = swCompModel.Extension
    Set swPartEnt = swModelDocExt.GetCorrespondingEntity(swCompEnt)
    Set swCompModel = swApp.ActivateDoc2(swCompModel.GetPathName, True, nRetval): Debug.Assert 0 = nRetval
```

```
    bRet = swPartEnt.Select4(False, Nothing)
```

```
    Debug.Print "File = " + swModel.GetPathName
    Debug.Print "  Component       = " + swComp.Name2 + " <" + swComp.ReferencedConfiguration + ">" + " [" + swComp.GetPathName + "]"
    Debug.Print "  Model           = " + swCompModel.GetPathName + " <" + swCompModelConfig.Name + ">"
```

```
End Sub
```
