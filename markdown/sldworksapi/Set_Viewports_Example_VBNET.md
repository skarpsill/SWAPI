---
title: "Set Viewports Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Viewports_Example_VBNET.htm"
---

# Set Viewports Example (VB.NET)

This example shows how to set viewports and check and change whether
they're linked.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
' 2. Set some breakpoints (e.g., before and after panning the viewports).
' 3. Open the Immediate window.
' 4. Press F5 at each breakpoint.
'
' Postconditions:
' 1. Sets viewport arrangement to Two View-Horizontal (* Top viewport is
'    panned; bottom viewport also panned because it is linked to top
'    viewport).
' 3. Unlinks viewports (Top viewport is panned; bottom view isn't panned
'    because viewports were unlinked).
' 4. Sets viewport arrangement to a single viewport.
' 5. Examine the Immediate window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelViewManager As ModelViewManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelView As ModelView

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set the viewport arrangement to Two View-Horizontal
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Set viewport arrangement to Two View-Horizontal...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelViewManager = swModel.ModelViewManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelViewManager.ViewportDisplay = swViewportDisplay_e.swViewportTwoViewHorizontal

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Check to see if the viewports are linked
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Are viewports linked? " & swModelViewManager.LinkedViews)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Pan the model in the top viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' The model in the bottom viewport also pans
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' because it's linked to the top viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Panning the model in top viewport; model in bottom viewport also pans because the viewports are linked...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView = swModel.ActiveView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.003875128205128, 0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.004982307692308, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.005535897435897, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.007196666666667, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006089487179487, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.004982307692308, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002214358974359, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001107179487179, -0.002214358974359)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, -0.004982307692308)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, -0.006643076923077)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, -0.006089487179487)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001107179487179, -0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.0005535897435897, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001107179487179, 0.003875128205128)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002767948717949, 0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, 0.006643076923077)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002767948717949, 0.005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.003875128205128, 0.006643076923077)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, 0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.001660769230769, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.003875128205128, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0160541025641, 0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.01273256410256, 0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002767948717949, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002767948717949, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.008857435897436, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.02435794871795, -0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.03044743589744, -0.002214358974359)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.01826846153846, -0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.01217897435897, -0.004982307692308)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.004428717948718, -0.004982307692308)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, -0.003875128205128)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.0005535897435897, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.008303846153846, 0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.009411025641026, 0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.01328615384615, 0.008303846153846)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.003875128205128, 0.007750256410256)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002767948717949, 0.007750256410256)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0.003875128205128)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006089487179487, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.008857435897436, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002767948717949, -0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.001660769230769, -0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.0005535897435897)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Fit the model in each viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ViewZoomtofit2()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Unlink the viewports
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Unlink the viewports...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelViewManager.LinkedViews = False
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Are viewports linked? " & swModelViewManager.LinkedViews)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Pan the model in the top viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' The model in the bottom viewport doesn't pan
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' because it's no longer linked to the top viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Panning the model in top viewport; model in bottom viewport doesn't pan because the viewports are no longer linked...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView = swModel.ActiveView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.003875128205128, 0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.004982307692308, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.005535897435897, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.007196666666667, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006089487179487, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.004982307692308, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002214358974359, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001107179487179, -0.002214358974359)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, -0.004982307692308)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, -0.006643076923077)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, -0.006089487179487)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001107179487179, -0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.0005535897435897, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001107179487179, 0.003875128205128)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002767948717949, 0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, 0.006643076923077)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002767948717949, 0.005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.003875128205128, 0.006643076923077)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, 0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.001660769230769, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.003875128205128, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0160541025641, 0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.01273256410256, 0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002767948717949, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.0005535897435897, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002767948717949, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.008857435897436, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.02435794871795, -0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.03044743589744, -0.002214358974359)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.01826846153846, -0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.01217897435897, -0.004982307692308)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.004428717948718, -0.004982307692308)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, -0.003875128205128)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.0005535897435897, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.001660769230769, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.002214358974359, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.008303846153846, 0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.009411025641026, 0.004428717948718)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.01328615384615, 0.008303846153846)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0.003875128205128, 0.007750256410256)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002767948717949, 0.007750256410256)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0.003875128205128)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006089487179487, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.008857435897436, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.006643076923077, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.002767948717949, -0.003321538461538)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.001660769230769, -0.001660769230769)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(-0.0005535897435897, -0.001107179487179)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, -0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.0005535897435897)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelView.TranslateBy(0, 0.0005535897435897)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Change the viewport arrangement back to a single viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelViewManager.ViewportDisplay = swViewportDisplay_e.swViewportSingle

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Fit the model in the viewport
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ViewZoomtofit2()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
