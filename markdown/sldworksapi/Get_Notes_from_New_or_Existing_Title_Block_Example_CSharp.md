---
title: "Get Notes from New or Existing Title Block (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm"
---

# Get Notes from New or Existing Title Block (C#)

This example shows how to create a title block in a drawing, if one
does not already exist, and how to get the notes from an existing title
block in a drawing.

```vb
//--------------------------------------------------------
// Preconditions: Drawing document is open.
//
// Postconditions: If the drawing contains a title block, then
// kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the notes of that block are printed
// kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}to the Immediate window. If not,
// kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}a title block is created.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
namespace ExampleCS.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDocExtension swExt;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SelectionMgr swSelMgr;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}View swView;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DrawingDoc swDraw;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc as ModelDoc2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager as SelectionMgr;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDraw = swModel as DrawingDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sheet swSheet;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSheet = swDraw.GetCurrentSheet() as Sheet;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}TitleBlock swTitleBlock;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swTitleBlock = swSheet.TitleBlock;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vNotes;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create title block if one doesn't exist
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swTitleBlock == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swView = swDraw.GetFirstView() as View;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}vNotes = (object[])swView.GetNotes();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Add first two notes to the title block
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}DispatchWrapper[] notesArray = new DispatchWrapper[2];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}notesArray[0] = new DispatchWrapper(vNotes[0]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}notesArray[1] = new DispatchWrapper(vNotes[1]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swTitleBlock = swSheet.InsertTitleBlock(notesArray);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vNotes = (object[])swTitleBlock.GetNotes();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i < vNotes.Length; i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Note swNote;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swNote = (Note)vNotes[i];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Name: " + swNote.GetName());
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Value: " + swNote.GetText());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
