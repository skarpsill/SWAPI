---
title: "Deselect Marked Entity Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Deselect_Marked_Entity_Example_VBNET.htm"
---

# Deselect Marked Entity Example (VB.NET)

## Deselect Marked Entity (VB.NET)

```
This example shows how to deselect a previously selected and marked entity.
```

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the Base-Extrude feature.
' 2. Examine the graphics area and FeatureManager
'    design tree to verify.
' 3. At Stop, press F5 to continue.
' 4. Deselects the Base-Extrude feature.
' 5. Examine the Immediate window, graphics
'    area, and FeatureManager design tree to verify.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDocSpecification As DocumentSpecification
        Dim swSelMgr As SelectionMgr
        Dim swModelExt As ModelDocExtension
        Dim bRet As Boolean
        Dim lMark As Integer
        Dim lMarkedIdx As Integer
        Dim lNumMarkedSelections As Integer
        Dim lNumAllSelections As Integer

        ' Open the document
        swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt")
        swModel = swApp.ActiveDoc
        If swModel Is Nothing Then
            swModel = swApp.OpenDoc7(swDocSpecification)
        End If

        swSelMgr = swModel.SelectionManager
        swModelExt = swModel.Extension
        ' Select the Base-Extrude feature and mark it with a a value of 8
        bRet = swModelExt.SelectByID2("Base-Extrude", "BODYFEATURE", 0, 0, 0, False, 8, Nothing, swSelectOption_e.swSelectOptionDefault)

        Stop
        ' Examine the graphics area to verify that Base-Extrude is selected
        ' Press F5 to continue

        ' Look for a given mark value
        lMark = 8
        ' Get the number of marked selections
        lNumMarkedSelections = swSelMgr.GetSelectedObjectCount2(lMark)
        Debug.Print("Number of marked selections = " & lNumMarkedSelections)

        ' Get the total number of selections
        lNumAllSelections = swSelMgr.GetSelectedObjectCount2(-1)
        Debug.Print("Number of selections        = " & lNumAllSelections)

        Debug.Print(" ")

        ' Deselect the marked selection
        For lMarkedIdx = 1 To lNumAllSelections
            Debug.Print("Selected object #" & lMarkedIdx & " deselected? " & swSelMgr.DeSelect2(lMarkedIdx, lMark))
        Next lMarkedIdx

        ' Examine the graphics area to verify that Base-Extrude is deselected

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
