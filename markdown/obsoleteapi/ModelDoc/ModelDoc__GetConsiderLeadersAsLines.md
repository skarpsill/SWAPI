---
title: "ModelDoc::GetConsiderLeadersAsLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetConsiderLeadersAsLines.htm"
---

# ModelDoc::GetConsiderLeadersAsLines

This method is obsolete
and has been superseded byModelDoc2::GetConsiderLeadersAsLines.

Description

This method determines if the display data of a
leader should be included as lines when the lines are retrieved from a
view or annotation in this document.

Syntax (OLE Automation)

retval = ModelDoc.GetConsiderLeadersAsLines
( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if leaders should be returned as line data,
FALSE if leaders should not be returned as line data |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetConsiderLeadersAsLines
( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if leaders should be returned as line data,
FALSE if leaders should not be returned as line data |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

The GetLeaderCount and GetLeaderAtIndex APIs that
are supported by several different annotations return the information
about where the vertices of the leader are located. The GetLineCount and
GetLinesAtIndex APIs also return the leader information as part of its
line information. Depending on what your program is trying to accomplish
and which APIs it is using, this duplication of information may not be
desirable. ModelDoc::SetConsiderLeadersAsLines controls this behavior
by setting a flag on the document that indicates whether or not the leader
information should be returned as part of the line information or not.

This API gets the current behavior for this document.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__GetConsiderLeadersAsLines.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
