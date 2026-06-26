---
title: "Get Precisions for a Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Precisions_for_a_Dimension_Example_VB.htm"
---

# Get Precisions for a Dimension Example (VBA)

This example shows how to get the precisions for a dimension.

```
'--------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\lesson2\tutor1.sldprt.
' 2. Right-click Annotations and click Show Feature Dimensions.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDispDim As SldWorks.DisplayDimension
    Dim swDim As SldWorks.Dimension
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    bRet = swModel.Extension.SelectByID2("D1@Fillet1@tutor1.SLDPRT", "DIMENSION", 1.27275536990925E-02, 2.29950387838887E-02, 7.75856501351018E-02, False, 0, Nothing, 0)
    Set swDispDim = swSelMgr.GetSelectedObject6(1, -1)
    Set swDim = swDispDim.GetDimension
    Debug.Print "Dim = " & swDim.FullName
    Debug.Print "  Nominal:"
    Debug.Print "    Primary      = " & swDispDim.GetPrimaryPrecision2
    Debug.Print "    Alternate    = " & swDispDim.GetAlternatePrecision2
    Debug.Print "  Tolerance:"
    Debug.Print "    Primary      = " & swDispDim.GetPrimaryTolPrecision2
    Debug.Print "    Alternate    = " & swDispDim.GetAlternateTolPrecision2
End Sub
```
