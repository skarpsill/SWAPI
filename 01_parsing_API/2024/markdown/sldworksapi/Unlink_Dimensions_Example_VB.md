---
title: "Unlink Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Unlink_Dimensions_Example_VB.htm"
---

# Unlink Dimensions Example (VBA)

This example shows how to unlink dimensions in a part.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\lesson2\tutor1.sldprt.
' 2. Right-click Annotations and click Show Feature Dimensions.
' 3. Right-click either 120 dimension and click Link Values.
' 4. Type AreaDimension and click OK.
' 5. Right-click the other 120 dimension and click Link Values.
' 6. Type AreaDimension and click OK.
' 7. Open the Immediate window.
'
' Postconditions:
' 1. Removes the links from the linked dimensions.
' 2. Examine the Immediate window and graphics area.
'
' NOTE:
' * This macro gets all dimensions in the part, including dimensions
'   that are not associated with a feature. These types of
'   dimensions usually appear under Annotations.
' * Because the part is used elsewhere, do not save changes.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeat As SldWorks.Feature
    Dim swDimen As SldWorks.Dimension
    Dim swDispDim As SldWorks.DisplayDimension
    Dim swDispDimAnn As SldWorks.Annotation
    Dim nRetval As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeat = swModel.FirstFeature
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Do While Not swFeat Is Nothing
        Set swDispDim = swFeat.GetFirstDisplayDimension
        If Not swDispDim Is Nothing Then
            Debug.Print "  " & swFeat.Name
        End If
        Do While Not swDispDim Is Nothing
            Set swDispDimAnn = swDispDim.GetAnnotation
            Set swDimen = swDispDim.GetDimension
            If swDispDim.IsLinked Then
                Debug.Print "    " & swDispDimAnn.GetName & " [" & swDimen.FullName & "] -- > " & swDispDim.GetLinkedText
                nRetval = swDispDim.Unlink: Debug.Assert swLinkDimensionError_NoError = nRetval
            End If
            Set swDispDim = swFeat.GetNextDisplayDimension(swDispDim)
        Loop
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
End Sub
```
