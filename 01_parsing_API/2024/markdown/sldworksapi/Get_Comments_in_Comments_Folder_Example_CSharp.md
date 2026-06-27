---
title: "Get Comments in Comments Folder Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Comments_in_Comments_Folder_Example_CSharp.htm"
---

# Get Comments in Comments Folder Example (C#)

This example shows how to add and get the comments in a Comments folder.

```
//----------------------------------------------
// Preconditions:
// 1. Verify that the specified model document
//    to open exists.
// 2. Open Immediate window.
//
// Postconditions:
// 1. Examine the FeatureManager design tree
//    to verify that the Comments folder is not
//    shown, then press F5.
// 2. Adds a comment to the Comments folder
//    and updates the FeatureManager design
//    tree.
// 3. Examine the FeatureManager design tree
//    to verify that the Comments folder is
//    shown, then press F5.
// 4. Prints the number of comments, name of the
//    the comments, and text of the comments
//    in the Comments folder to the Immediate
//    window. Examine the Immediate window.
//
// NOTE: Because this model document is used
// elsewhere, do not save changes.
//---------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace UpdateFeatureTreeCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            {
                ModelDoc2 swModelDoc = default(ModelDoc2);
                Feature swFeat = default(Feature);
                FeatureManager swFeatMgr = default(FeatureManager);
                CommentFolder swCommentFolder = default(CommentFolder);
                Comment swComment = default(Comment);
                int nbrComments = 0;
                string sFeatType = null;
                object[] vComments = null;
                string fileName = null;
                int errors = 0;
                int warnings = 0;
                long i = 0;

                // Open part document
                fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.sldprt";
                swModelDoc = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

                // Traverse the FeatureManager design tree for Comments folder

                // Get first feature in FeatureManager design tree
                swFeat = (Feature)swModelDoc.FirstFeature();
                swFeatMgr = (FeatureManager)swModelDoc.FeatureManager;

                System.Diagnostics.Debugger.Break();
                // Examine FeatureManager design tree to verify that
                // the the Comments folder is not shown; press F5

                while ((swFeat != null))
                {
                    sFeatType = swFeat.GetTypeName();

                    // If Comments folder, add a comment
                    if (sFeatType == "CommentsFolder")
                    {
                        swCommentFolder = (CommentFolder)swFeat.GetSpecificFeature2();

                        // Add comment and update FeatureManager design tree
                        // so that Comments folder is shown
                        swComment = (Comment)swCommentFolder.AddComment("First comment in comment folder.");
                        swFeatMgr.UpdateFeatureTree();

                        System.Diagnostics.Debugger.Break();
                        // Locate Comments folder in FeatureManager design; press F5

                        // Get number of comments in Comment folder
                        nbrComments = swCommentFolder.GetCommentCount();
                        Debug.Print("Number of comments in Comments folder         = " + nbrComments);

                        vComments = (object[])swCommentFolder.GetComments();
                        for (i = 0; i <= (nbrComments - 1); i++)
                        {
                            swComment = (Comment)vComments[i];
                            Debug.Print("Name of comment in FeatureManager design tree = " + swComment.Name);
                            Debug.Print("Text of comment                               = " + swComment.Text);
                            Debug.Print("");
                        }
                    }

                    // Get next feature in FeatureManager design tree
                    swFeat = (Feature)swFeat.GetNextFeature();

                }
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
