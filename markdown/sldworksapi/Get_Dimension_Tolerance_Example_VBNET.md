---
title: "Get Dimension Tolerance Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Tolerance_Example_VBNET.htm"
---

# Get Dimension Tolerance Example (VB.NET)

This example shows how to get and set dimension tolerance values and options.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.slddrw.
' 2. Open the Immediate window.
' 3. Zoom in on the diameter dimension and click it.
'
' Postconditions:
' 1. Sets the dimension tolerance type to fit with tolerance.
' 2. Sets the dimension fit tolerance type to transitional.
' 3. Gets the minimum and maximum dimension tolerances for the
'    selected dimension and whether the values are valid.
' 4. Gets the height and scale of the font of the dimension
'    tolerances.
' 5. Sets the dimension fit tolerance font to be the same
'    size as the dimension tolerance font.
' 6. Gets the height and scale of the font of the dimension fit
'    tolerance.
' 7. Examine the Immediate window and drawing sheet.
'
' NOTE: Because this drawing is used elsewhere, do not save changes.
'--------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim swDimension As Dimension
        Dim swDimensionTolerance As DimensionTolerance
        Dim maxValue As Double
        Dim minValue As Double
        Dim maxValueValid As Integer
        Dim minValueValid As Integer
        Dim fontHeight As Double
        Dim fontScale As Double

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager

        'Get the selection
        swDisplayDimension = swSelMgr.GetSelectedObject6(1, 0)

        'If selection is not a dimension, then exit
        If swSelMgr.GetSelectedObjectType3(1, -1) <> swSelectType_e.swSelDIMENSIONS Then Exit Sub

        'Selection is a dimension, so get the dimension tolerance object
        swDimension = swDisplayDimension.GetDimension2(0)
        swDimensionTolerance = swDimension.Tolerance

        'Set tolerance type to fit with tolerance and transitional
        swDimensionTolerance.Type = swTolType_e.swTolFITWITHTOL
        Debug.Print("Type of tolerance (8 = swTolType_e.swTolFITWITHTOL): " & swDimensionTolerance.Type)
        swDimensionTolerance.FitType = swFitType_e.swFitTRANSITIONAL
        Debug.Print("Type of fit tolerance (2 = swFitType_e.swFitTransitional): " & swDimensionTolerance.FitType)
        Debug.Print("")

        'Get dimension tolerance minimum and maximum values
        'and whether values are valid
        maxValueValid = swDimensionTolerance.GetMaxValue2(maxValue)
        minValueValid = swDimensionTolerance.GetMinValue2(minValue)
        Debug.Print("Minimum dimension tolerance of " & minValue & " valid (0 = valid)? " & minValueValid)
        Debug.Print("Maximum dimension tolerance of " & maxValue & " valid (0 = valid)? " & maxValueValid)

        'Get some dimension tolerance values
        fontHeight = swDimensionTolerance.GetFontHeight
        Debug.Print("  Height of font: " & fontHeight * 1000.0# & " mm")
        fontScale = swDimensionTolerance.GetFontScale
        Debug.Print("  Scale of font: " & fontScale)
        Debug.Print("")

        'Set and get some dimension fit tolerance values
        swDimensionTolerance.SetFitFont(True, False, 0)
        Debug.Print("Dimension fit tolerance font same size as tolerance font? " & swDimensionTolerance.GetFitFontUseDimension)
        fontHeight = swDimensionTolerance.GetFitFontHeight
        Debug.Print("  Height of fit tolerance font: " & fontHeight * 1000.0# & " mm")
        fontScale = swDimensionTolerance.GetFitFontScale
        Debug.Print("  Scale of fit tolerance font: " & fontScale)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
