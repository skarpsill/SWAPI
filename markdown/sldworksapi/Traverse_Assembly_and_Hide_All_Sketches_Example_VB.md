---
title: "Traverse Assembly and Hide All Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_and_Hide_All_Sketches_Example_VB.htm"
---

# Traverse Assembly and Hide All Sketches Example (VBA)

This example shows how to traverse an assembly and hide all sketches.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. In the FeatureManager design tree, show some sketches by
'    expanding a component, expanding one or more features
'    in that component, right-clicking each sketch in each of
'    the expanded features, and clicking Show in each
'    context-sensitive menu.
' 3. Examine the graphics area and locate the shown sketches.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Hides all shown sketches in the assembly.
' 3. Examine the Immediate window and the graphics area.
'------------------------------------------------------------------
Option Explicit
```

```
Sub BlankSketchFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swFeat As SldWorks.Feature)
    Dim bRet  As Boolean
    If "ProfileFeature" = swFeat.GetTypeName Then
        bRet = swFeat.Select2(False, 0): Debug.Assert bRet
        swModel.BlankSketch
    End If
End Sub
```

```
Sub TraverseFeatureFeatures(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swFeat As SldWorks.Feature, nLevel As Long)
    Dim swSubFeat As SldWorks.Feature
    Dim swSubSubFeat As SldWorks.Feature
    Dim swSubSubSubFeat As SldWorks.Feature
    Dim sPadStr As String
    Dim i As Long
```

```
    For i = 0 To nLevel
        sPadStr = sPadStr + "  "
    Next i
```

```
    Dim bRet As Boolean
```

```
    If "Annotations" <> swFeat.Name Then
        bRet = swFeat.Select2(True, 0): Debug.Assert bRet
    End If
```

```
    While Not swFeat Is Nothing
        Debug.Print sPadStr + swFeat.Name + " [" + swFeat.GetTypeName + "]"
        BlankSketchFeature swApp, swModel, swFeat
        Set swSubFeat = swFeat.GetFirstSubFeature
        While Not swSubFeat Is Nothing
            Debug.Print sPadStr + "  " + swSubFeat.Name + " [" + swSubFeat.GetTypeName + "]"
            BlankSketchFeature swApp, swModel, swSubFeat
            Set swSubSubFeat = swSubFeat.GetFirstSubFeature
            While Not swSubSubFeat Is Nothing
                Debug.Print sPadStr + "    " + swSubSubFeat.Name + " [" + swSubSubFeat.GetTypeName + "]"
                BlankSketchFeature swApp, swModel, swSubSubFeat
                Set swSubSubSubFeat = swSubFeat.GetFirstSubFeature
                While Not swSubSubSubFeat Is Nothing
                    Debug.Print sPadStr + "      " + swSubSubSubFeat.Name + " [" + swSubSubSubFeat.GetTypeName + "]"
                    BlankSketchFeature swApp, swModel, swSubSubSubFeat
                    Set swSubSubSubFeat = swSubSubSubFeat.GetNextSubFeature()
                Wend
                Set swSubSubFeat = swSubSubFeat.GetNextSubFeature()
            Wend
            Set swSubFeat = swSubFeat.GetNextSubFeature()
        Wend
        Set swFeat = swFeat.GetNextFeature
    Wend
End Sub
```

```
Sub TraverseComponentFeatures(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2, nLevel As Long)
    Dim swFeat As SldWorks.Feature

    Set swFeat = swComp.FirstFeature
    TraverseFeatureFeatures swApp, swModel, swFeat, nLevel
End Sub
```

```
Sub TraverseComponent(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2, nLevel As Long)
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
        Debug.Print sPadStr & "+" & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & ">"
        TraverseComponentFeatures swApp, swModel, swChildComp, nLevel
        TraverseComponent swApp, swModel, swChildComp, nLevel + 1
    Next i
End Sub
```

```
Sub TraverseModelFeatures(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, nLevel As Long)
    Dim swFeat As SldWorks.Feature

    Set swFeat = swModel.FirstFeature
    TraverseFeatureFeatures swApp, swModel, swFeat, nLevel
End Sub
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim nStart As Long
    Dim bRet As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConf = swModel.GetActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
```

```
    nStart = Timer
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' Traverse the assembly and hide all shown sketches
    TraverseModelFeatures swApp, swModel, 1
    TraverseComponent swApp, swModel, swRootComp, 1
```

```
    Debug.Print ""
    Debug.Print "Time to traverse the assembly = " & Timer - nStart & " seconds"
```

```
End Sub
```
