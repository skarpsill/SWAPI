---
title: "Suppress Component Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suppress_Component_Feature_Example_VB.htm"
---

# Suppress Component Feature Example (VBA)

This example shows how to suppress the selected component feature.

```
'------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select a component feature in the FeatureManager
'    design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Suppressed the selected component feature.
' 2. Prints the names of the assembly and the suppressed
'    component feature to the Immediate window.
' 3. Examine the Immediate window.
'
' NOTE: Editing a component requires that geometry on
' the component be selected. However, not
' all features are associated with geometry.
' Therefore, it is necessary to select the component
' before attempting to edit the component.
'------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp               As SldWorks.SldWorks
    Dim swModel             As SldWorks.ModelDoc2
    Dim swAssy              As SldWorks.AssemblyDoc
    Dim swEditModel         As SldWorks.ModelDoc2
    Dim swEditPart          As SldWorks.PartDoc
    Dim swEditAssy          As SldWorks.AssemblyDoc
    Dim swSelMgr            As SldWorks.SelectionMgr
    Dim swFeat              As SldWorks.Feature
    Dim swComp              As SldWorks.Component2
    Dim featName            As String
    Dim status              As Long
    Dim info                As Long
    Dim retVal              As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1): Debug.Assert Not swFeat Is Nothing
```

```
    Set swComp = swSelMgr.GetSelectedObjectsComponent2(1): Debug.Assert Not swComp Is Nothing
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "    " & swFeat.Name & " <" & swFeat.GetTypeName & ">"
    Debug.Print ""
```

```
    featName = swFeat.Name
```

```
    retVal = swComp.Select2(False, 0): Debug.Assert retVal
    status = swAssy.EditPart2(True, False, info): Debug.Assert swEditPartSuccessful = status
```

```
    Set swEditModel = swAssy.GetEditTarget
```

```
    Select Case swEditModel.GetType
```

```
        Case swDocPART
            Set swEditPart = swEditModel
            Set swFeat = swEditPart.FeatureByName(featName): Debug.Assert Not swFeat Is Nothing
            retVal = swFeat.Select2(False, 0): Debug.Assert retVal
```

```
        Case swDocASSEMBLY
```

```
            Set swEditAssy = swEditModel
            Set swFeat = swEditAssy.FeatureByName(featName): Debug.Assert Not swFeat Is Nothing
            retVal = swFeat.Select2(False, 0): Debug.Assert retVal
```

```
        Case Else
```

```
            Debug.Assert False
```

```
    End Select
```

```
    ' Suppress the selected feature
    retVal = swEditModel.EditSuppress2: Debug.Assert retVal
    swAssy.EditAssembly
```

```
End Sub
```
