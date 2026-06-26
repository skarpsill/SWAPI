---
title: "Display Hidden Lines in Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Hidden_Lines_in_Drawing_Example_VBNET.htm"
---

# Display Hidden Lines in Drawing Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc

         swModel = swApp.ActiveDoc
         swDraw = swModel

         ' Display mode settings
         swDraw.ViewDisplayHidden()
         Stop
         swDraw.ViewDisplayHiddengreyed()
         Stop
         swDraw.ViewDisplayWireframe()
         Stop
         swDraw.ViewDisplayShaded()
         Stop

         ' Suppress view
         swDraw.SuppressView()
         Stop
         ' Display an X where the view was suppressed
         swDraw.HideShowDrawingViews()
         Stop
         ' Unsuppress view
         swDraw.UnsuppressView()

     End Sub

     Public swApp As SldWorks

 End Class
```
