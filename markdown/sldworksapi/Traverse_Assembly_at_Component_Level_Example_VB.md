---
title: "Traverse Assembly at Component Level Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_at_Component_Level_Example_VB.htm"
---

# Traverse Assembly at Component Level Example (VBA)

This example shows how to traverse an assembly at the component level.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Specified assembly document opens.
' 2. Traverses the components in the assembly.
' 3. Examine the Immediate window.
'------------------------------------------------------
Option Explicit
```

```
Sub TraverseComponent _
(swComp As SldWorks.Component2, nLevel As Long)
```

```
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
    vChildComp = swComp.GetChildren
    For i = 0 To UBound(vChildComp)
        Set swChildComp = vChildComp(i)
        TraverseComponent swChildComp, nLevel + 1
        Debug.Print sPadStr & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & ">"
    Next i
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
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\stepped_shaft.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    Set swConf = swModel.GetActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' Traverse components
    TraverseComponent swRootComp, 1
```

```
End Sub
```
