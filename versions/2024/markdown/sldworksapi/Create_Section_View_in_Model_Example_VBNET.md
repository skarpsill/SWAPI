---
title: "Create Section View in Model Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Section_View_in_Model_Example_VBNET.htm"
---

# Create Section View in Model Example (VB.NET)

This example shows how to create a section view in a model.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_bridge.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Displays a section view with three sections that
'    are capped in color.
' 2. Examine the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------

			Imports SolidWorks.Interop.sldworks

			Imports SolidWorks.Interop.swconst

			Imports System.Runtime.InteropServices

			Imports System

			Imports System.Diagnostics

			Partial Class SolidWorksMacro

			    Dim swModel As ModelDoc2

			    Dim swModelDocExt As ModelDocExtension

			    Dim swModelViewMgr As ModelViewManager

			    Dim swSelMgr As SelectionMgr

			    Dim svData As SectionViewData

			    Dim plane1 As Feature, plane2 As Feature, plane3 As Feature

			    Dim boolstatus As Boolean

			    Sub main()

			        swModel = swApp.ActiveDoc

			        swModelDocExt = swModel.Extension

			        swModelViewMgr = swModel.ModelViewManager

			        swSelMgr = swModel.SelectionManager

			        boolstatus = swModelDocExt.SelectByID2("Front", "PLANE",
			-0.04751707843116, 0.04466659468449, 0.1209999999999, False, 1, Nothing,
			0)

			        boolstatus = swModelDocExt.SelectByID2("Top", "PLANE",
			-0.06781533387408, 0.00100317525596, 0.1263684575364, True, 2, Nothing,
			1)

			        boolstatus = swModelDocExt.SelectByID2("Right", "PLANE",
			-0.000808330303073, 0.07304457560201, -0.003890984556108, True, 4, Nothing,
			1)

			        svData = swModelViewMgr.CreateSectionViewData()

			        FillPlaneData(svData, swSelMgr)

			        boolstatus = swModelViewMgr.CreateSectionView(svData)

			        Debug.Print(" Section
			bodies are valid: " & boolstatus)

			    End Sub

			    Sub FillPlaneData(ByVal data As SectionViewData, ByVal selMgr As SelectionMgr)

			        plane1 = selMgr.GetSelectedObject6(1, 0)

			        plane2 = selMgr.GetSelectedObject6(2, 0)

			        plane3 = selMgr.GetSelectedObject6(4, 0)

			        data.FirstPlane = plane1

			        data.FirstReverseDirection = False

			        data.FirstOffset =
			-0.01

			        data.FirstRotationX = 0.296705972839036

			        data.FirstRotationY = 0.174532925199433

			        data.FirstColor = RGB(255, 0, 0)

			        data.SecondPlane = plane2

			        data.SecondReverseDirection = False

			        data.SecondOffset =
			0.01

			        data.SecondRotationX = 0.296705972839036

			        data.SecondRotationY = 0.174532925199433

			        data.SecondColor = RGB(0, 255, 0)

			        data.ThirdPlane = plane3

			        data.ThirdReverseDirection = True

			        data.ThirdOffset =
			-0.01

			        data.ThirdRotationX = 0.296705972839036

			        data.ThirdRotationY = 0.174532925199433

			        data.ThirdColor = RGB(0, 0, 255)

			        data.Redraw = True

			        data.ShowSectionCap = True

			        data.KeepCapColor = True

			        data.GraphicsOnlySection = True

			    End Sub

			    Public swApp As SldWorks

			End Class
```
