---
title: "Set Fully Resolved Assembly to Lightweight Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Fully_Resolved_Assembly_to_Lightweight_Example_VB.htm"
---

# Set Fully Resolved Assembly to Lightweight Example (VBA)

This example shows how to set a fully resolved assembly to lightweight.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open a fully resolved assembly document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sets all assembly components to lightweight.
' 2. Examine the Immediate window and FeatureManager design tree.
'----------------------------------------------------------------
```

```
Sub SetComponentLightWeight(sPadStr As String, swComp As SldWorks.Component2)
```

```
    Dim vChildArr As Variant
    Dim swChildComp As SldWorks.Component2
    Dim swChildModel As SldWorks.ModelDoc2
    Dim nRetVal As Long
    Dim nDocType As Long
    Dim i As Long
```

```
    Debug.Print sPadStr & swComp.Name2 & " [" & CBool(swComp.Visible) & "]"
```

```
    vChildArr = swComp.GetChildren
    For i = 0 To UBound(vChildArr)
        Set swChildComp = vChildArr(i)
        ' Is Nothing if another instance has been previously set to lightweight
        Set swChildModel = swChildComp.GetModelDoc2
        If Not swChildModel Is Nothing Then
            nDocType = swChildModel.GetType
        Else
            nDocType = swDocNONE
        End If
```

```
        nRetVal = swChildComp.SetSuppression2(swComponentLightweight)
        If swDocPART = nDocType Or swDocNONE = nDocType Then
            Debug.Assert swResolveNotPerformed = nRetVal
        Else
            ' Cannot set a sub-assembly to lightweight; must set each part to lightweight
            Debug.Assert swDocASSEMBLY = swChildModel.GetType
            Debug.Assert swResolveError = nRetVal
        End If
```

```
        ' Recurse into this component
        SetComponentLightWeight sPadStr & "  ", swChildComp
```

```
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swAssy                      As SldWorks.AssemblyDoc
    Dim swConfig                    As SldWorks.Configuration
    Dim swConfigMgr                 As SldWorks.ConfigurationManager
    Dim swRootComp                  As SldWorks.Component2
    Dim bRet                        As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
    Debug.Print "File = " & swModel.GetPathName
    SetComponentLightWeight "  ", swRootComp
```

```
    ' Update in-context features
    bRet = swModel.ForceRebuild3(False): Debug.Assert bRet
```

```
End Sub
```
