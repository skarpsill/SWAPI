---
title: "Set Body for View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Body_for_View_Example_CSharp.htm"
---

# Set Body for View Example (C#)

This example shows how to show just one body of a multibody part in
a drawing view.

```vb
//------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
 // 2. Save the part document as a drawing document:
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click File > Make Drawing from Part.
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Click OK on the Sheet Format/Size dialog.
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Drag the *Isometric view from the View Palette onto
 // kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}the drawing sheet.
 // 3. Select the drawing view.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Shows one body of the multibody part
 //    in the drawing view.
 // 2. Examine the drawing and the Immediate window.
 //
 // NOTE: Because the part document is used elsewhere, do not save
 // changes.
 //------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Windows.Forms;
namespace BodiesViewCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidWorks.Interop.sldworks.View swView = default(SolidWorks.Interop.sldworks.View);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrBodies = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] arrBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Body2 swBody = default(Body2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2 swFace = default(Face2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Entity swEnt = default(Entity);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectData swSelData = default(SelectData);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PartDoc swPart = default(PartDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool status = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DispatchWrapper[] arrBodiesIn = new DispatchWrapper[1];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] Bodies = new object[1];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int objType = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = (SolidWorks.Interop.sldworks.View)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swView == null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MessageBox.Show("View not selected.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrBodies = swView.GetBodiesCount();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Number of bodies: " + nbrBodies);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((nbrBodies < 1))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MessageBox.Show("No bodies in selected view.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrBody = (object[])swView.Bodies;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i < arrBody.Length; i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swBody = (Body2)arrBody[i];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swSelData = (SelectData)swSelMgr.CreateSelectData();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swSelData.View = swView;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}status = swBody.Select2(false, swSelData);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Object type 76 is a solid body
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}objType = swSelMgr.GetSelectedObjectType3(1, -1);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((objType == 76))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Object type: solid body");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((!((int)swSelectType_e.swSelSOLIDBODIES == swSelMgr.GetSelectedObjectType3(1, -1))))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}MessageBox.Show("Solid body not found.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFace = (Face2)swBody.GetFirstFace();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}while ((swFace != null))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swEnt = (Entity)swFace;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// Select using IEntity
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}status = swEnt.Select4(true, swSelData);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Assert(status);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swFace = (Face2)swFace.GetNextFace();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Name of body: " + swBody.GetSelectionId());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the bodies from referenced model
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swView.ReferencedDocument;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrBody = (object[])swPart.GetBodies2((int)swBodyType_e.swSolidBody, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((nbrBodies == 1))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swView.Bodies = (arrBody);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Set the body to include in the drawing view
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Bodies[0] = arrBody[0];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}arrBodiesIn[0] = new DispatchWrapper(Bodies[0]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swView.Bodies = (arrBodiesIn);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
