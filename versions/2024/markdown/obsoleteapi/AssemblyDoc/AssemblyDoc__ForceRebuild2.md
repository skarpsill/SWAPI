---
title: "AssemblyDoc::ForceRebuild2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__ForceRebuild2.htm"
---

# AssemblyDoc::ForceRebuild2

This
method is obsolete and has been superseded by[ModelDoc2::ForceRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ForceRebuild3.htm).

Description

This method forces a rebuild of the assembly.

Syntax (OLE Automation)

void AssemblyDoc.ForceRebuild2 (topOnly)

(Table)=========================================================

| Input: | (BOOL) topOnly | TRUE if you want to
rebuild the top level of assembly only; FALSE if you want to rebuild the
top level and all subassemblies |
| --- | --- | --- |

Syntax (COM)

status = AssemblyDoc->ForceRebuild2 ( topOnly
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) topOnly | TRUE if you want to rebuild the top level of
assembly only; FALSE if you want to rebuild the top level and all subassemblies |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This command rebuilds the entire model, whether
or not it needs to be rebuilt. This operation can be very time consuming.
Use the topLevelOnly argument to enhance performance.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$ZEditRebuild$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDoc\AssemblyDoc__ForceRebuild2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
