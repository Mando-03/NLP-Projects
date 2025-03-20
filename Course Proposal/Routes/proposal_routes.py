from flask import Blueprint, request, jsonify

from LLM import get_model
from Prompt import get_course_proposal_prompt

proposal_bp = Blueprint('proposal', __name__)


@proposal_bp.route('/proposal', methods=['POST'])
def generate_course_proposal():
    '''
    Generate a course proposal based on the provided course details. 
    '''
    try:
        course_details = request.json
        if not course_details:
            return jsonify({'error': 'No course details provided.'}), 400
        prompt = get_course_proposal_prompt(course_details)
        model = get_model()
        proposal = model.generate_content(prompt)
        return jsonify({
            'proposal': proposal.text
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
