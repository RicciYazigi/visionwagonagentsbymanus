import pytest
from vision_wagon.agents.operational.eroswriter_agent import ErosWriterAgent
from vision_wagon.agents.operational.assembly_agent import AssemblyAgent
from vision_wagon.agents.executive.adult_compliance_agent import AdultComplianceAgent
from vision_wagon.agents.operational.traffic_capture_agent import TrafficCaptureAgent

# Mock BaseAgent if necessary, or ensure it's available
# For simplicity, assuming BaseAgent is correctly implemented and available

@pytest.fixture
def eros_writer_agent():
    return ErosWriterAgent()

@pytest.fixture
def assembly_agent():
    return AssemblyAgent()

@pytest.fixture
def adult_compliance_agent():
    return AdultComplianceAgent()

@pytest.fixture
def traffic_capture_agent():
    return TrafficCaptureAgent()

def test_eros_writer_agent_capabilities(eros_writer_agent):
    assert eros_writer_agent.has_capability("cultural_adaptation")
    assert eros_writer_agent.has_capability("cliffhanger_creation")
    assert eros_writer_agent.has_capability("character_consistency")

def test_eros_writer_agent_generate_narrative(eros_writer_agent):
    narrative = eros_writer_agent.generate_narrative("a romantic encounter", "Spanish")
    assert "romantic encounter" in narrative
    assert "culturally adapted for Spanish" in narrative

def test_assembly_agent_capabilities(assembly_agent):
    assert assembly_agent.has_capability("erotic_content_assembly")
    assert assembly_agent.has_capability("create_multimedia_erotic_content")

def test_assembly_agent_assemble_multimedia_package(assembly_agent):
    package = assembly_agent.assemble_multimedia_package(
        "test narrative", ["img1.jpg"], "audio.mp3"
    )
    assert package["narrative"] == "test narrative"
    assert "img1.jpg" in package["images"]
    assert package["audio"] == "audio.mp3"
    assert package["metadata"]["age_rating"] == "18+"

def test_adult_compliance_agent_capabilities(adult_compliance_agent):
    assert adult_compliance_agent.has_capability("age_verification_meta_check")
    assert adult_compliance_agent.has_capability("jurisdiction_filter")
    assert adult_compliance_agent.has_capability("platform_policy_check")

def test_adult_compliance_agent_run_compliance_check_compliant(adult_compliance_agent):
    multimedia_package = {
        "narrative": "A mild erotic story.",
        "metadata": {"age_rating": "18+"}
    }
    assert adult_compliance_agent.run_compliance_check(multimedia_package, "US", ["OnlyFans"])

def test_adult_compliance_agent_run_compliance_check_non_compliant_age(adult_compliance_agent):
    multimedia_package = {
        "narrative": "A mild erotic story.",
        "metadata": {"age_rating": "16+"}
    }
    assert not adult_compliance_agent.run_compliance_check(multimedia_package, "US", ["OnlyFans"])

def test_adult_compliance_agent_run_compliance_check_non_compliant_jurisdiction(adult_compliance_agent):
    multimedia_package = {
        "narrative": "An explicit sexual act.",
        "metadata": {"age_rating": "18+"}
    }
    assert not adult_compliance_agent.run_compliance_check(multimedia_package, "Germany", ["OnlyFans"])

def test_traffic_capture_agent_capabilities(traffic_capture_agent):
    assert traffic_capture_agent.has_capability("teaser_generation")
    assert traffic_capture_agent.has_capability("social_media_posting")
    assert traffic_capture_agent.has_capability("engagement_monitoring")

def test_traffic_capture_agent_generate_teaser(traffic_capture_agent):
    multimedia_package = {"narrative": "This is a test narrative. It has multiple sentences."}
    teaser = traffic_capture_agent.generate_teaser(multimedia_package)
    assert "¡Prepárate para una experiencia inolvidable!" in teaser
    assert "This is a test narrative." in teaser

def test_traffic_capture_agent_social_media_posting(traffic_capture_agent):
    result = traffic_capture_agent.social_media_posting("Test teaser", "Facebook")
    assert result["status"] == "success"
    assert result["platform"] == "Facebook"
    assert "post_url" in result

def test_traffic_capture_agent_engagement_monitoring(traffic_capture_agent):
    result = traffic_capture_agent.engagement_monitoring("http://example.com/post/123")
    assert "likes" in result
    assert "comments" in result
    assert "shares" in result


