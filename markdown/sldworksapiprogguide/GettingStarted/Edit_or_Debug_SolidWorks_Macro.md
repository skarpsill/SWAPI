---
title: "Edit or Debug SOLIDWORKS Macro"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Edit_or_Debug_SolidWorks_Macro.htm"
---

# Edit or Debug SOLIDWORKS Macro

Edit or debug SOLIDWORKS macros using Microsoft VBA or Microsoft VSTA.

NOTES:

- [SOLIDWORKS 2018 offers Visual
  Studio Tools for Applications (VSTA)](VSTA_2015.htm), impacting how VB.NET and C# macros are
  developed and run in SOLIDWORKS 2018 and later.
- When debugging Microsoft VSTA macros with user-interface
  components such as PropertyManager pages, manipulators, or other objects
  that use events or handler objects, the debugger must continue to run
  after the main() method of the VSTA macro exits. Either deselect the user-interface
  system optionStop VSTA debugger on macro
  exit(located on theTools >Options >SystemOptionsdialog) or set swUserPreferenceToggle_e
  swStopDebuggingVstaOnExit to false to keep the debugger running after
  the main() method of the Microsoft VSTA macro exits.
- To
  automatically edit a macro after recording it, clickTools
  >Options >SystemsOptions.
  On theGeneraltab, selectAutomatically edit macro after recordingand clickOK. This setting is
  persistent across SOLIDWORKS sessions unless you selected to save a just
  recorded macro asSW All Macros Types
  (*.swp, *.csproj, *.vbproj). This setting has no effect when you
  select to save a macro as multiple macro types.
- If
  you recently edited the macro, you can select it from the menu when you
  clickTools >Macro.
  This menu lists the last nine macros that you edited.

#### To edit or debug a SOLIDWORKS VBA macro:

1. ClickEdit Macroon the Macro toolbar, or clickTools
  >Macro >Edit.

1. In the dialog, selectSW VBA Macros (*.swp)in Files of type
  (selected by default).
2. Click

  Open

  .

#### To edit a .NET macro

Read[SOLIDWORKS 2018 offers Visual Studio Tools for
Applications (VSTA)](VSTA_2015.htm).

#### New macro tasks

- Delete extra lines
  of code automatically inserted in the macro when it was created:
- [Explicitly
  declare all variables](Option_Explicit_Statement.htm)in a Microsoft VBA macro.
- [Early
  bind all variables](Early_and_Late_Binding.htm).

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic1" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="RecordSolidWorksMacro$$**$$RunSolidWorksMacro$$**$$AssignSolidWorksMacroShortcutKeyMenu$$**$$AssignSolidWorksMacroButton$$**$$VBAMacroOverview$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\GettingStarted\Edit_or_Debug_SolidWorks_Macro.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
