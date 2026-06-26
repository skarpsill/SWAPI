---
title: "Get BOM Balloon Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_BOM_Balloon_Properties_Example_CSharp.htm"
---

# Get BOM Balloon Properties Example (C#)

This example shows how to get the properties of a BOM balloon.

```
//----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Inserts a BOM table.
// 3. Inserts a BOM balloon.
// 4. Gets and sets the BOM ballon's properties.
// 5. Examine the Immediate window.
//
// NOTE: Because this assembly is used elsewhere, do not save
// changes.
//-----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace BomTableAnnotationCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Note swNote = default(Note);
            Annotation swAnnotation = default(Annotation);
            object[] attachedEntityArray = null;
            int[] attachedEntityTypeArray = null;
            Entity swEntity = default(Entity);
            Component2 swComponent = default(Component2);
            ModelDoc2 swComponentModel = default(ModelDoc2);
            BomTableAnnotation swBomTableAnnotation = default(BomTableAnnotation);
            BalloonOptions swBomBalloonParams = default(BalloonOptions);
            int i = 0;
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            //Open assembly, create BOM table, and select BOM balloon
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bladed shaft.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swBomTableAnnotation = (BomTableAnnotation)swModelDocExt.InsertBomTable3("C:\\Program Files\\SolidWorks Corp\\SolidWorks\\lang\\english\\bom-standard.sldbomtbt", 618, 568, (int)swBomType_e.swBomType_TopLevelOnly, "", false, (int)swNumberingType_e.swNumberingType_None, false);
            status = swModelDocExt.SelectByID2("", "FACE", 0.0139294427590926, 0.059464184169542, 0.0082768338148469, false, 0, null, 0);
            swBomBalloonParams = (BalloonOptions)swModelDocExt.CreateBalloonOptions();
            swBomBalloonParams.Style = (int)swBalloonStyle_e.swBS_SplitCirc;
            swBomBalloonParams.Size = (int)swBalloonFit_e.swBF_Tightest;
            swNote = swModelDocExt.InsertBOMBalloon2(swBomBalloonParams);
            status = swModelDocExt.SelectByID2("DetailItem2@Annotations", "NOTE", 0.00431152692774954, 0.0699703491909496, 0.0033561420724473, false, 0, null, 0);

            //Get and set BOM balloon properties
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, -1);
            swAnnotation = (Annotation)swNote.GetAnnotation();
            attachedEntityArray = (object[])swAnnotation.GetAttachedEntities2();
            attachedEntityTypeArray = (int[])swAnnotation.GetAttachedEntityTypes();
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("  Name = " + swAnnotation.GetName());
            swNote.SetBomBalloonText((int)swDetailingNoteTextContent_e.swDetailingNoteTextCustom, "ABC", (int)swDetailingNoteTextContent_e.swDetailingNoteTextCustom, "EFG");
            Debug.Print("    Upper text = " + swNote.GetBomBalloonText(true) + " [" + swNote.GetBomBalloonTextStyle(true) + "]");
            Debug.Print("    Lower text = " + swNote.GetBomBalloonText(false) + " [" + swNote.GetBomBalloonTextStyle(false) + "]");
            Debug.Print("    Balloon fit = " + swNote.GetBalloonSize());
            Debug.Print("    Balloon style = " + swNote.GetBalloonStyle());
	    Debug.Print("    Balloon padding = " + swNote.GetBalloonPadding());
            Debug.Print("    Is stacked? " + swNote.IsStackedBalloon());
            Debug.Print("    Is stacked master? " + swNote.IsStackedBalloonMaster());
            for (i = 0; i < attachedEntityArray.Length; i++)
            {
                Debug.Print("    Attached entity type = " + attachedEntityTypeArray[i]);
                if (attachedEntityTypeArray != null)
                {
                    swEntity = (Entity)attachedEntityArray[i];
                    swComponent = (Component2)swEntity.GetComponent();
                    swComponentModel = (ModelDoc2)swComponent.GetModelDoc();
                    Debug.Print("    Attached entity = " + swComponent.GetPathName() + " <" + swComponent.ReferencedConfiguration + ">" + " --> " + swComponentModel.GetPathName());
                }
            }

            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
