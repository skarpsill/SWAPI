---
title: "SldWorks::AddToolbarCommand"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddToolbarCommand.htm"
---

# SldWorks::AddToolbarCommand

This method is obsolete and has been superseded
by[SldWorks::AddToolbarCommand2](sldworksAPI.chm::/SldWorks/SldWorks__AddToolbarCommand2.htm).

Description

This method specifies the application functions called by a toolbar
button or sets a button to be a separator.

Syntax (OLE Automation)

retval = SldWorks.AddToolbarCommand
( moduleName, toolbarId, toolbarIndex, commandString )

(Table)=========================================================

| Input: | (BSTR) moduleName | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long) toolbarId | Toolbar ID from SldWorks::AddToolbar |
| Input: | (int) toolbarIndex | Zero based index of the bitmap button |
| Input: | (BSTR) commandString | Command string for the button (see Remarks) |
| Return: | (BOOLEAN) retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->AddToolbarCommand
( moduleName, toolbarId, toolbarIndex, commandString, &retval )

(Table)=========================================================

| Input: | (BSTR) moduleName | Name of the module (that is. USERDLL). |
| --- | --- | --- |
| Input: | (long) toolbarId | Toolbar ID from SldWorks::AddToolbar |
| Input: | (int) toolbarIndex | Zero based index of the bitmap button |
| Input: | (BSTR)c ommandString | Command string for the button (see Remarks) |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

Call this method for each of the buttons in the toolbar to specify the
functions that get called by SolidWorks when the button is pressed and
to check if the button is enabled. The button is not displayed until this
method is called.

To add a separator to a toolbar, set the commandString argument to an
empty string. A button bitmap must still be defined in the Toolbar for
the separator.

The commandString argument specifies which function to call when this
button is selected by the user. The syntax is as follows:

"function@updatefunction,hintstring\ntooltipstring"

where:

function is the name of the function that
gets called when the user presses the button. This function must also
be declared as an EXPORT in your .def file.

updatefunction is optional and is used
to control the state of the button. If an update function is specified,
then it must be declared as an EXPORT in your .def file. This update function
is called from SolidWorks in reaction to Frame changes (that is. the user
switches from an active Drawing to a Part document). The button display
is controlled by the return value from your update function as follows:

return 0; // Button is disabled
(grey)

return 1; // Button is enabled. This
is the default state with if no update function is specified.

return 2 // Button is Disabled and
"Pushed"

return 3 // Button is Enabled and
"Pushed

hintstring is optional and is shown in
the SolidWorks status bar when the user moves their mouse over this particular
button. If a hint string is specified, it must be preceded by a comma
as shown in the following example.

tooltipstring is optional and appears
in a popup tooltip window if the user leaves the mouse on the button without
pressing a mouse button. If a tooltip string is specified, it must be
preceded by a \nas shown in
the following exmaple.

Example:

"AddBox@checkForUserSelects,This
function adds a box\nAdd Box"

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SldWorks\SldWorks__AddToolbarCommand.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Toolbar_Creation_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SldWorks\SldWorks__AddToolbarCommand.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
