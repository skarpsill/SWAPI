---
title: "Get Dimension Values in Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Values_in_Drawing_Example_VBNET.htm"
---

# Get Dimension Values in Drawing Example (VB.NET)

This example shows how to get the values of the dimensions in a drawing.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc
         Dim swView As View
         Dim swDispDim As DisplayDimension
         Dim swDim As Dimension
         Dim swAnn As Annotation

         swModel = swApp.ActiveDoc
         swDraw = swModel

         Debug.Print("File = " & swModel.GetPathName)

         swView = swDraw.GetFirstView

         Do While Not swView Is  Nothing
             Debug.Print("  View = " & swView.Name)

             swDispDim = swView.GetFirstDisplayDimension5

             Do While Not swDispDim Is Nothing
                 swAnn = swDispDim.GetAnnotation
                 swDim = swDispDim.GetDimension

                 Debug.Print("    ------------------------------------")
                 Debug.Print("    AnnName = " & swAnn.GetName)
                 Debug.Print("      DimFullName                  = " & swDim.FullName)
                 Debug.Print("      DimName                      = " & swDim.Name)
                 Debug.Print("      swDimensionParamType_e type  = " & swDim.GetType)
                 Debug.Print("      DrivenState                  = " & swDim.DrivenState)
                 Debug.Print("      ReadOnly                     = " & swDim.ReadOnly)
                 Debug.Print("      Value                        = " & swDim.GetSystemValue2(""))
                 Debug.Print("")
                 Debug.Print("      Arrowside                    = " & swDispDim.ArrowSide)
                 Debug.Print("      TextAll                      = " & swDispDim.GetText(swDimensionTextParts_e.swDimensionTextAll))
                 Debug.Print("      TextPrefix                   = " & swDispDim.GetText(swDimensionTextParts_e.swDimensionTextPrefix))
                 Debug.Print("      TextSuffix                   = " & swDispDim.GetText(swDimensionTextParts_e.swDimensionTextSuffix))
                 Debug.Print("      CalloutAbove                 = " & swDispDim.GetText(swDimensionTextParts_e.swDimensionTextCalloutAbove))
                 Debug.Print("      CalloutBelow                 = " & swDispDim.GetText(swDimensionTextParts_e.swDimensionTextCalloutBelow))

                 swDispDim = swDispDim.GetNext3

             Loop

             swView = swView.GetNextView

         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
