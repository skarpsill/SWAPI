---
title: "Get Linked Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Linked_Dimensions_Example_VB.htm"
---

# Get Linked Dimensions Example (VBA)

This example shows how to get the linked dimensions in a part document.

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
' 1. Examine the Immediate window.
' 2. Click either 120 dimension, change 120 to 150, and press Enter.
' 3. Changes the other 120 dimension to 150 because the dimensions
'    are linked.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------
Option Explicit
```

```
Private Type DimLink
    Name As String
    DimName() As String
End Type
```

```
Private Sub ProcessDimLinkList(ThisDimLinkList() As DimLink)
    Dim i As Long
    Dim j As Long
```

```
    For i = 0 To UBound(ThisDimLinkList)
        Debug.Print ThisDimLinkList(i).Name
        For j = 0 To UBound(ThisDimLinkList(i).DimName)
            Debug.Print "  " & ThisDimLinkList(i).DimName(j)
        Next j
    Next i
End Sub
```

```
Private Sub AddToDimLinkList(ThisDimLink As DimLink, ThisDimLinkList() As DimLink)
    Debug.Assert UBound(ThisDimLink.DimName) = 0
    Dim i  As Long
```

```
    For i = 0 To UBound(ThisDimLinkList)
        If ThisDimLinkList(i).Name = ThisDimLink.Name Then
        ReDim Preserve ThisDimLinkList(i).DimName(UBound(ThisDimLinkList(i).DimName) + 1)
            ThisDimLinkList(i).DimName(UBound(ThisDimLinkList(i).DimName)) = ThisDimLink.DimName(0)
            Exit Sub
        End If
    Next i
```

```
    If 0 = UBound(ThisDimLinkList) And "" = ThisDimLinkList(0).Name Then
        ThisDimLinkList(0).Name = ThisDimLink.Name
        ThisDimLinkList(0).DimName(UBound(ThisDimLinkList(0).DimName)) = ThisDimLink.DimName(0)
        Exit Sub
    End If
```

```
    ReDim Preserve ThisDimLinkList(UBound(ThisDimLinkList) + 1)
    ReDim Preserve ThisDimLinkList(UBound(ThisDimLinkList)).DimName(0)
```

```
    ThisDimLinkList(UBound(ThisDimLinkList)).Name = ThisDimLink.Name
    ThisDimLinkList(UBound(ThisDimLinkList)).DimName(UBound(ThisDimLinkList(UBound(ThisDimLinkList)).DimName)) = ThisDimLink.DimName(0)
End Sub
```

```
Private Function IsInDimLinkList(ThisDimLink As DimLink, ThisDimLinkList() As DimLink) As Boolean
    Dim i As Long
    Dim j As Long
```

```
    For i = 0 To UBound(ThisDimLinkList)
        If ThisDimLinkList(i).Name = ThisDimLink.Name Then
            For j = 0 To UBound(ThisDimLinkList(i).DimName)
                If ThisDimLinkList(i).DimName(j) = ThisDimLink.DimName(0) Then
                    IsInDimLinkList = True
                    Exit Function
                End If
            Next j
        End If
    Next i
End Function
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
    Dim OneDimLink As DimLink
    Dim DimLinkList() As DimLink
    Dim bRet As Boolean
```

```
    ReDim DimLinkList(0)
    ReDim DimLinkList(0).DimName(0)
    ReDim OneDimLink.DimName(0)
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
                OneDimLink.Name = swDispDim.GetLinkedText
                OneDimLink.DimName(0) = swDimen.FullName
                Debug.Print "    " & swDispDimAnn.GetName & " [" & swDimen.FullName & "] -- > " & swDispDim.GetLinkedText
```

```
                If Not IsInDimLinkList(OneDimLink, DimLinkList) Then
                    AddToDimLinkList OneDimLink, DimLinkList
                End If
            End If
            Set swDispDim = swFeat.GetNextDisplayDimension(swDispDim)
        Loop
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
    ProcessDimLinkList DimLinkList
```

```
End Sub
```
