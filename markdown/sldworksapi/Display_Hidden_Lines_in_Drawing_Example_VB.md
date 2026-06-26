---
title: "Display Hidden Lines in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Hidden_Lines_in_Drawing_Example_VB.htm"
---

# Display Hidden Lines in Drawing Example (VBA)

This example shows how to set the display mode of a drawing view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document.
 ' 2. Select a view.
 ' 3. Inspect the graphics area and press F5 six times.
 '
 ' Postconditions: The display mode, hide/show, and suppression
 ' settings for the document are modified as specified.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                           As SldWorks.SldWorks
     Dim swModel                         As SldWorks.ModelDoc2
     Dim swDraw As SldWorks.DrawingDoc
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
    ' Display mode settings
     swDraw.ViewDisplayHidden
     Stop
     swDraw.ViewDisplayHiddengreyed
     Stop
     swDraw.ViewDisplayWireframe
     Stop
     swDraw.ViewDisplayShaded
     Stop

    ' Suppress view
     swDraw.SuppressView
     Stop
     ' Display an X where the view was suppressed
     swDraw.HideShowDrawingViews
     Stop
     ' Unsuppress view
     swDraw.UnsuppressView
End Sub
```
