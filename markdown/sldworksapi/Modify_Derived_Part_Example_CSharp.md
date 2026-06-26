---
title: "Modify Derived Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Derived_Part_Example_CSharp.htm"
---

# Modify Derived Part Example (C#)

This example shows how to insert and modify a derived part.

```
//-----------------------------------------------
// Preconditions:
// 1. Verify that the part documents to open and insert exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Inserts a derived part in the part document
//    opened in step 1.
// 3. Changes some parameters of the derived part feature.
// 4. Examine the Immediate window.
//
// NOTE: Because both part documents are used elsewhere,
// do not save any changes.
//-----------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DerivedPartFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Component2 swComp = default(Component2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swDerivedFeat = default(Feature);
            Feature swFeat = default(Feature);
            DerivedPartFeatureData swDerivedData = default(DerivedPartFeatureData);
            bool bRet = false;
            string fileName = null;
            string derivedFileName = null;
            int errors = 0;
            int warnings = 0;

            //Open part, insert another part, and select the derived part feature
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\holecube.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            derivedFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swPart = (PartDoc)swModel;
            swFeat = (Feature)swPart.InsertPart3(derivedFileName, (int)swInsertPartOptions_e.swInsertPartImportSolids, "Default" );
            swModel.ClearSelection2(true);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swModelDocExt.SelectByID2("box", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            //Get the selected derived part feature
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swDerivedFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent3(1, -1);
            Debug.Print("Name of derived part feature = " + swDerivedFeat.Name);
            Debug.Print("");
            //Get and modify import planes with derived part
            bRet = TestImportPlane(swDerivedFeat, swModel, swComp);
            Debug.Print("");
            //Get and modify import absorbed sketches with derived part
            bRet = TestImportAbsorbedSketches(swDerivedFeat, swModel, swComp);
            Debug.Print("");
            //Get and modify import unabsorbed sketches with derived part
            bRet = TestImportUnAbsorbedSketches(swDerivedFeat, swModel, swComp);
            Debug.Print("");
            swDerivedData = (DerivedPartFeatureData)swDerivedFeat.GetDefinition();
            Debug.Print("Derived file's path and name = " + swDerivedData.PathName);

        }

        public bool TestImportPlane(Feature feat, ModelDoc2 doc, Component2 comp)
        {
            DerivedPartFeatureData featData = default(DerivedPartFeatureData);
            bool startVal = false;
            bool boolstatus = false;

            featData = (DerivedPartFeatureData)feat.GetDefinition();
            startVal = featData.ImportPlane;
            Debug.Print("Import planes with derived part? " + startVal);
            featData.ImportPlane = true;
            Debug.Print("Modified import planes with derived part? " + featData.ImportPlane);
            boolstatus = feat.ModifyDefinition(featData, doc, comp);
            featData = null;
            return boolstatus;
        }

        public bool TestImportAbsorbedSketches(Feature feat, ModelDoc2 doc, Component2 comp)
        {
            DerivedPartFeatureData featData = default(DerivedPartFeatureData);
            bool startVal = false;
            bool boolstatus = false;

            featData = (DerivedPartFeatureData)feat.GetDefinition();
            startVal = featData.ImportAbsorbedSketches;
            Debug.Print("Import absorbed sketches with derived part? " + startVal);
            featData.ImportAbsorbedSketches = true;
            Debug.Print("Modified import absorbed sketches with derived part? " + featData.ImportAbsorbedSketches);
            boolstatus = feat.ModifyDefinition(featData, doc, comp);
            featData = null;
            return boolstatus;
        }

        public bool TestImportUnAbsorbedSketches(Feature feat, ModelDoc2 doc, Component2 comp)
        {
            DerivedPartFeatureData featData = default(DerivedPartFeatureData);
            bool startVal = false;
            bool boolstatus = false;

            featData = (DerivedPartFeatureData)feat.GetDefinition();
            startVal = featData.ImportUnAbsorbedSketches;
            Debug.Print("Import unabsorbed sketches with derived part? " + startVal);
            featData.ImportUnAbsorbedSketches = true;
            Debug.Print("Modified import unabsorbed sketches with derived part? " + featData.ImportUnAbsorbedSketches);
            boolstatus = feat.ModifyDefinition(featData, doc, comp);
            featData = null;
            return boolstatus;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
