---
title: "Obsolete and New Block Objects, Methods, and Properties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Miscellaneous/Obsolete_and_New_Block_Objects,_Methods,_and_Properties.htm"
---

# Obsolete and New Block Objects, Methods, and Properties

IBlockDefinition and IBlockInstance interfaces are obsolete and unsupported
as of SOLIDWORKS 2007 and later. To create blocks in drawings, parts,
and assemblies, use ISketchBlockDefinition and ISketchBlockInstance.

The following list identifies the now obsolete and unsupported block-related
objects, methods, and properties and their replacements. You must migrate
any code that creates blocks using the now obsolete block interfaces to
the new block interfaces.

(Table)=========================================================

| Obsolete API | New API |
| --- | --- |
| IBlockDefinition APIs IBlockDefinition::GetBasePoint IBlockDefinition::GetBlockInstanceCount IBlockDefinition::GetDimensionCount IBlockDefinition::GetDimensions IBlockDefinition::GetExternalFileName IBlockDefinition::GetNoteCount IBlockDefinition::GetNotes IBlockDefinition::GetSketch IBlockDefinition::GetUseExternalFileName IBlockDefinition::InsertInstance IBlockDefinition::Name IBlockDefinition::SetBasePoint IBlockDefinition::SetExternalFileName IBlockDefinition::SetUseExternalFile | ISketch APIs ISketch::GetSketchBlockInstanceCount ISketch::GetSketchBlockInstances ISketchBlockDefinition APIs ISketchBlockDefinition::FileName ISketchBlockDefinition::GetArcCount ISketchBlockDefinition::GetArcs ISketchBlockDefinition::GetDisplayDimensionCount ISketchBlockDefinition::GetDisplayDimensions ISketchBlockDefinition::GetEllipseCount ISketchBlockDefinition::GetEllipses ISketchBlockDefinition::GetFeature ISketchBlockDefinition::GetInstanceCount ISketchBlockDefinition::GetInstances ISketchBlockDefinition::GetLineCount ISketchBlockDefinition::GetLines ISketchBlockDefinition::GetNoteCount ISketchBlockDefinition::GetNotes ISketchBlockDefinition::GetParabolaCount ISketchBlockDefinition::GetSketch ISketchBlockDefinition::InsertionPoint ISketchBlockDefinition::LinkToFile ISketchBlockDefinition::GetParabolaCount ISketchBlockDefinition::GetParabolas ISketchBlockDefinition::GetSplineCount ISketchBlockDefinition::GetSplines2 ISketchBlockDefinition::GetUserPointsCount ISketchBlockDefinition::GetUserPoints ISketchBlockDefinition::Save |
| IBlockInstance APIs IBlockInstance::Angle IBlockInstance::Definition IBlockInstance::GetAnnotation IBlockInstance::GetAttributeCount IBlockInstance::GetAttributes IBlockInstance::GetAttributeValue IBlockInstance::GetNext IBlockInstance::SetAttributeValue IBlockInstance::Scale2 IBlockInstance::TextDisplay | ISketchBlockInstance APIs ISketchBlockInstance::Angle ISketchBlockInstance::BlockToSketchTransform ISketchBlockInstance::Definition ISketchBlockInstance::DisplayDimension ISketchBlockInstance::GetArrowheadStyle ISketchBlockInstance::GetAttributeCount ISketchBlockInstance::GetAttributes ISketchBlockInstance::GetAttributeValue ISketchBlockInstance::GetLeaderStyle ISketchBlockInstance::GetSketch ISketchBlockInstance::InstancePosition ISketchBlockInstance::Layer ISketchBlockInstance::Name ISketchBlockInstance::Select ISketchBlockInstance::SetAttributeValue ISketchBlockInstance::SetLeader ISketchBlockInstance::Scale ISketchBlockInstance::TextDisplay |
| IDrawingDoc APIs IDrawingDoc::CreateBlockDefinition IDrawingDoc::MakeBlockDefinition IDrawingDoc::ExplodeBlockInstance IDrawingDoc::GetBlockDefinition IDrawingDoc::GetBlockDefinitions IDrawingDoc::GetBlockDefinitionCount IDrawingDoc::GetEditBlock IDrawingDoc::InsertBlock IDrawingDoc::SaveBlock | ISketchManager APIs ISketchManager::MakeSketchBlockFromFile ISketchManager::MakeSketchBlockFromSelected ISketchManager::MakeSketchBlockFromSketch ISketchManager::ExplodeSketchBlockInstance ISketchManager::GetSketchBlockDefinitions ISketchManager::GetSketchBlockDefinitionCount ISketchManager::EditSketchBlock ISketchManager::EndEditSketchBlock ISketchManager::InsertSketchBlockInstance ISketchBlockDefinition::Save |
| INote::IsAttribute | None |
| IView::GetFirstBlockInstance | None |

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic4" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="BlockDefinitionsBlockInstances$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\Miscellaneous\Obsolete_and_New_Block_Objects,_Methods,_and_Properties.htm">
<param name="_ID" value="RelatedTopic4">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
