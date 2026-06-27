---
title: "Set Display Mode of View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Display_Mode_of_View_Example_VBNET.htm"
---

# Set Display Mode of View Example (VB.NET)

This example shows how to set the display mode of a drawing view.

```vb
  '-------------------------------------
 ' Preconditions:
 ' 1. Open a drawing and select a drawing view.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the selected view's current display mode.
 ' 2. Resets the display mode.
 ' 3. Gets the new display mode.
 ' 4. Examine the Immediate window and graphics area.
  '--------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

           Dim swModel  As  ModelDoc2
           Dim swDraw  As  DrawingDoc
           Dim swSheet  As  Sheet
           Dim swView  As  View
           Dim swSelectionMgr   As   SelectionMgr

          swModel = swApp.ActiveDoc
          swDraw = swModel
          swSheet = swDraw.GetCurrentSheet
          swSelectionMgr = swModel.SelectionManager

          swView = swSelectionMgr.GetSelectedObject6(1, -1)

           Debug.Print("=====Current Display Mode======")
           Debug.Print("")

           Dim UseParentProp   As   Boolean
          UseParentProp = swView.GetUseParentDisplayMode
           Debug.Print("Using parent view mode?  " & UseParentProp)

           Dim displayMode   As   Long
          displayMode = swView.GetDisplayMode2
           Debug.Print("Current display mode as defined by swDisplayMode_e:  " & displayMode)

           Dim Facetted  As  Boolean
          Facetted = swView.GetFacettedHlrDisplay
           Debug.Print("Faceted (draft quality)?:  " & Facetted)

           Dim EdgesMode   As   Boolean
          EdgesMode = swView.GetDisplayEdgesInShadedMode
           Debug.Print("Display edges when the view is in shaded mode?  " & EdgesMode)

           Dim cThreadQuality   As   Boolean
          cThreadQuality = swView.GetCThreadQuality
           Debug.Print("Precision cosmetic thread dislay quality? " & cThreadQuality)

           'Reset display mode: Do not use parent view's display mode, shaded mode, draft quality, no edges displayed, precision cosmetic threads
          swView.SetDisplayMode4(False, 3,   True,   False,   True)

           Debug.Print("")
           Debug.Print("=====After Setting Display Mode======")
           Debug.Print("")
           Debug.Print("Using parent view mode?  " & swView.GetUseParentDisplayMode)
           Debug.Print("Current display mode as defined by swDisplayMode_e:  " & swView.GetDisplayMode2)
           Debug.Print("Faceted (draft quality)?  " & swView.GetFacettedHlrDisplay)
           Debug.Print("Display edges when view is in shaded mode?  " & swView.GetDisplayEdgesInShadedMode)
           Debug.Print("Precision cosmetic thread dislay quality? " & swView.GetCThreadQuality)

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
