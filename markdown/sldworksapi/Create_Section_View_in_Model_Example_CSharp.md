---
title: "Create Section View in Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Section_View_in_Model_Example_CSharp.htm"
---

# Create Section View in Model Example (C#)

This example shows how to create a section view in a model.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\multibody\multi_bridge.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Displays a section view with three sections that
//    are capped in color.
// 2. Examine the graphics area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------------------

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	using System;

	using System.Diagnostics;

	using Microsoft.VisualBasic;

	namespace GraphicsOnlySectionView_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 swModel;

	        ModelDocExtension swModelDocExt;

	        ModelViewManager swModelViewMgr;

	        SelectionMgr swSelMgr;

	        SectionViewData svData;

	        Feature plane1;

	        Feature plane2;

	        Feature plane3;

	        bool boolstatus;

	        public void Main()

	        {

	            swModel = (ModelDoc2)swApp.ActiveDoc;

	            swModelDocExt = swModel.Extension;

	            swModelViewMgr = swModel.ModelViewManager;

	            swSelMgr = (SelectionMgr)swModel.SelectionManager;

	            boolstatus = swModelDocExt.SelectByID2("Front", "PLANE",
	-0.04751707843116, 0.04466659468449, 0.1209999999999, false, 1, null, 0);

	            boolstatus = swModelDocExt.SelectByID2("Top", "PLANE",
	-0.06781533387408, 0.00100317525596, 0.1263684575364, true, 2, null, 1);

	            boolstatus = swModelDocExt.SelectByID2("Right", "PLANE",
	-0.000808330303073, 0.07304457560201, -0.003890984556108, true, 4, null, 1);

	            svData = swModelViewMgr.CreateSectionViewData();

	            FillPlaneData(svData, swSelMgr);

	            boolstatus = swModelViewMgr.CreateSectionView(svData);

	            Debug.Print("
	Section bodies are valid: " + boolstatus);

	        }

	        public void FillPlaneData(SectionViewData data, SelectionMgr selMgr)

	        {

	            plane1 = (Feature)selMgr.GetSelectedObject6(1,
	0);

	            plane2 = (Feature)selMgr.GetSelectedObject6(2,
	0);

	            plane3 = (Feature)selMgr.GetSelectedObject6(4,
	0);

	            data.FirstPlane = plane1;

	            data.FirstReverseDirection = false;

	            data.FirstOffset = -0.01;

	            data.FirstRotationX = 0.296705972839036;

	            data.FirstRotationY = 0.174532925199433;

	            data.FirstColor = Information.RGB(255, 0, 0);

	            data.SecondPlane = plane2;

	            data.SecondReverseDirection = false;

	            data.SecondOffset = 0.01;

	            data.SecondRotationX = 0.296705972839036;

	            data.SecondRotationY = 0.174532925199433;

	            data.SecondColor = Information.RGB(0, 255, 0);

	            data.ThirdPlane = plane3;

	            data.ThirdReverseDirection = true;

	            data.ThirdOffset = -0.01;

	            data.ThirdRotationX = 0.296705972839036;

	            data.ThirdRotationY = 0.174532925199433;

	            data.ThirdColor = Information.RGB(0, 0, 255);

	            data.Redraw = true;

	            data.ShowSectionCap = true;

	            data.KeepCapColor = true;

	            data.GraphicsOnlySection = true;

	        }

	        public SldWorks swApp;

	    }

	}
```
