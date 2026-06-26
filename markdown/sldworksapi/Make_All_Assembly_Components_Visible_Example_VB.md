---
title: "Make All Assembly Components Visible Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_All_Assembly_Components_Visible_Example_VB.htm"
---

# Make All Assembly Components Visible Example (VBA)

This example shows how to make all assembly components visible.

```
'---------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Hide a component (right-click the component in
'    the FeatureManager design tree and click the
'    Hide Components button.
' 3. Open the Immediate window.
'
'
' Postconditions:
' 1. Shows the hidden component.
' 2. Examine the Immediate window, FeatureManager
'    design tree, and graphics area.
'---------------------------------------
Option Explicit
```

```
Sub TraverseComponent(swComp As SldWorks.Component2, nLevel As Long)
```

```
    Dim vChildCompArr As Variant
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim swCompConfig As SldWorks.Configuration
    Dim sPadStr As String
    Dim i As Long
```

```
    For i = 0 To nLevel - 1
        sPadStr = sPadStr + "  "
    Next i
```

```
    vChildCompArr = swComp.GetChildren
    For Each vChildComp In vChildCompArr
        Set swChildComp = vChildComp
        Debug.Print sPadStr & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & ">"
        If swComponentHidden = swChildComp.Visible Then
            swChildComp.Visible = swComponentVisible
        End If
        TraverseComponent swChildComp, nLevel + 1
    Next
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConf = swModel.GetActiveConfiguration
    Set swRootComp = swConf.GetRootComponent
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    TraverseComponent swRootComp, 1
```

```
End Sub
```
