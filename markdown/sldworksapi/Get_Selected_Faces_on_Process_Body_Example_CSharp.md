---
title: "Get Selected Faces on Processed Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Faces_on_Process_Body_Example_CSharp.htm"
---

# Get Selected Faces on Processed Body Example (C#)

This example shows how to get the selected faces on a processed body.

```
//------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template
//    and part exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Creates a new part with an imported body
//    from the processed body of the original part.
// 3. Gets the body in the new part and selects
//    multiple faces on that body.
// 4. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//--------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
            const double RadPerDeg = 1.0 / 57.3;
            const double MaxUAngle = 1.0 * RadPerDeg;
            const double MaxVAngle = 1.0 * RadPerDeg;

            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Body2 swBody = default(Body2);
            Body2 swProcBody = default(Body2);
            PartDoc swPart = default(PartDoc);
            PartDoc swNewPart = default(PartDoc);
            Feature swFeat = default(Feature);
            object[] vBodies = new object[1];
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            bool status = false;
            object[] swBodyVar = new object[1];
            object[] swSelFaceVar = new object[4];
            int swSelFaceCount = 0;

            //Open part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swPart = (PartDoc)swModel;

            //Get and process body in part
            vBodies = (object[])swPart.GetBodies2((int)swBodyType_e.swSolidBody, false);
            swBody = (Body2)vBodies[0];
            swProcBody = (Body2)swBody.GetProcessedBody2(MaxUAngle, MaxVAngle);

            //Create new part containing processed body
            swNewPart = (PartDoc)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2014\\templates\\part.prtdot", 0, 0, 0);
            swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swProcBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck);
            Debug.Print("Original part: " + swModel.GetPathName());
            Debug.Print("  Title: " + swModel.GetTitle());
            Debug.Print("    Body faces: " + swBody.GetFaceCount());
            Debug.Print("    Processed body faces: " + swProcBody.GetFaceCount());

            //Select multiple faces in new part
            swModel = (ModelDoc2)swNewPart;
            Debug.Print("New part title: " + swModel.GetTitle());
            Debug.Print("    Body faces: " + swBody.GetFaceCount());
            Debug.Print("    Processed body faces: " + swProcBody.GetFaceCount());
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.0258707587273648, -0.00453920675113295, -0.00750000000022055, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.016247803762667, 0, -0.0112417538793466, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0149546544521968, -0.026689891165347, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0208314165242882, -0.0200000000001523, -0.00322480979224338, true, 0, null, 0);

            //Get selected faces in body
            swBodyVar = (object[])swNewPart.GetBodies2((int)swBodyType_e.swAllBodies, true);
            if ((swBodyVar == null))
            {
                Debug.Print("    Did not get any bodies.");
            }
            else
            {
                swBody = (Body2)swBodyVar[0];
                Debug.Print("    Name of processed body: " + swBody.Name);
            }
            swProcBody = (Body2)swBody.GetProcessedBodyWithSelFace();
            swSelFaceVar = (object[])swProcBody.GetSelectedFaces();
            if ((swSelFaceVar != null))
            {
                swSelFaceCount = swProcBody.GetSelectedFaceCount();
                Debug.Print("      Number of faces selected in processed body: " + swSelFaceCount);
            }
            else
            {
                Debug.Print("      No faces selected in processed body.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
