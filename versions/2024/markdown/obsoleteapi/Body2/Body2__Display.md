---
title: "Body2::Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__Display.htm"
---

# Body2::Display

This method is obsolete and superseded by[Body2::Display2](Body2__Display2.htm).

Description

This method displays a temporary body object in the context of the specified
part.

Syntax (OLE Automation)

void Body2.Display ( part, color)

(Table)=========================================================

| Input: | (LPDISPATCH) part | Pointer to Dispatch object, the part |
| --- | --- | --- |
| Input: | (long) color | Part color |

Syntax (COM)

status = Body2->IDisplay ( part,
color )

(Table)=========================================================

| Input: | (LPPARTDOC) part | Pointer to the part |
| --- | --- | --- |
| Input: | (long) color | Part color |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

While SolidWorks is displaying your body object using Body2::Display,
do not release it explicitly or implicitly. Before releasing or allowing
the Body2 object to be released, call Body2::Hide to prevent it from being
displayed.

COM applications can call Body2->Release() to avoid explicitly releasing
the Body2 object while it is being displayed.

Dispatch applications should avoid:

- allowing the Body2 object to go out of scope while
  it is being displayed.
- explicitly releasing the Body2 object by calling
  ReleaseDispatch while it is being displayed by SolidWorks.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
dtcid=2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Body2\Body2__Display.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
dtcid=3
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Body2\Body2__Display.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
