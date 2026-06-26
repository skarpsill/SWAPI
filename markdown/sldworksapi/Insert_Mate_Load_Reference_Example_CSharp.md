---
title: "Insert Mate Load Reference Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Mate_Load_Reference_Example_CSharp.htm"
---

# Insert Mate Load Reference Example (C#)

This example shows how to insert a mate load reference.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Gets the mate where to add a load reference.
// 3. Selects a supplemental face for the load reference.
// 4. Inserts a mate load reference.
// 5. Examine the Immediate window.
//
// NOTE: Because the assembly document is used elsewhere, do
// not save changes.
//-------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MateLoadReferenceCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Mate2 swMate = default(Mate2);
            MateLoadReference swMateLoadRef = default(MateLoadReference);
            Feature swFeat = default(Feature);
            Component2 swComponent = default(Component2);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            bool status = false;

            //Open the assembly document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\wrench.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssemblyDoc = (AssemblyDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get the mate where to add the load reference
            status = swModelDocExt.SelectByID2("Concentric4", "MATE", 0, 0, 0, false, 0, null, 0);
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, 0);
            swMate = (Mate2)swFeat.GetSpecificFeature2();

            //Insert the load reference using the selected mate and supplemental face
            status = swModelDocExt.SelectByID2("", "FACE", 0.087090587167495, -0.00524931403344908, 0.00483048001655106, true, 0, null, 0);
            swMateLoadRef = (MateLoadReference)swAssemblyDoc.InsertLoadReference(swMate);
            Debug.Print("Name of load reference added to " + swFeat.Name + " mate = " + swMateLoadRef.Name);
            Debug.Print("Number of supplemental faces of the mate load reference for Component1 = " + swMateLoadRef.GetFacesCount(0));
            swComponent = (Component2)swMateLoadRef.get_Component(0);
            Debug.Print("Name of Component1 = " + swComponent.Name2);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
